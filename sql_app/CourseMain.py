from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import schemas, models, crud
from Validation import Datavalidation
import Validation

router = APIRouter(tags= ["Course"])

models.Base.metadata.create_all(bind = engine)

app = FastAPI()


def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()




# create course
@router.post("/CreateCou/")
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    if db.query(models.Course).filter(models.Course.cid == course.cid).first():
        raise HTTPException(status_code=409, detail="Course already exists")
    
    # Valid Data
    Validation.Errors = {}
    Datavalidation.check_CID(course.cid)
    Datavalidation.check_CNAME(course.CName)
    Datavalidation.check_DEPARTMENT(course.Department)
    Datavalidation.chek_CREDIT(course.Credit)
    if len(Validation.Errors) != 0:
        return Validation.Errors
    return crud.create_course(db=db, course=course)



# read course
@router.get("/GetCou/{course_cid}", response_model= schemas.Course)
def read_course(course_id : int, db: Session = Depends(get_db)):

    db_course = crud.get_course(db, course_id = course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course Not Found !")
    return db_course



# delete course
@router.delete("/DeleteCou/{course_cid}")
def delete_course(course_cid: int, db: Session = Depends(get_db)):
    with Session(engine) as session:
        course = session.get(models.Course, course_cid)
        if not course:
            raise HTTPException(status_code=404, detail="Course Not Found !")
        session.delete(course)
        session.commit()
        return "deleted successfully!"



# update course
@router.patch("/UpdateCou/{course_cid}")
def update_course(course_cid : int, course: schemas.CourseUpdate, db:Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id = course_cid)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course Not Found !")
    course_data = course.model_dump(exclude_unset= True)

    # Valid Data
    Validation.Errors = {}
    if "CName" in course_data:
        Datavalidation.check_CNAME(course_data["CName"])
    if "Department" in course_data:
        Datavalidation.check_DEPARTMENT(course_data["Department"])
    if "Credit" in course_data:
        Datavalidation.chek_CREDIT(course_data["Credit"])

    if len(Validation.Errors) != 0:
        return Validation.Errors
    
    for key, value in course_data.items():
        setattr(db_course, key, value)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course