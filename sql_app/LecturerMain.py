from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import schemas, models, crud
from Validation import Datavalidation
import Validation

router = APIRouter(tags= ["Lecturer"])

models.Base.metadata.create_all(bind = engine)

app = FastAPI()


def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close


# Create Lecturer
@router.post("/CreateLE/")
def create_Lecturer(lecturer: schemas.Lecturer, db: Session = Depends(get_db)):

    db_lecturer = crud.get_lecture(db, lecturer_id = lecturer.LID)
    if db_lecturer:
        raise HTTPException(status_code=409, detail="Lecturer Number already exists")
    Validation.Errors = {}
    Datavalidation.check_LID(lecturer.LID)
    Datavalidation.check_FNAME(lecturer.FName)
    Datavalidation.check_LNAME(lecturer.LName)
    Datavalidation.check_ID(lecturer.ID)
    Datavalidation.check_DEPARTMENT(lecturer.Department)
    Datavalidation.check_MAJOR(lecturer.Major)
    Datavalidation.check_BIRTH(lecturer.Birth)
    Datavalidation.check_BornCity(lecturer.BornCity)
    Datavalidation.check_Address(lecturer.Address)
    Datavalidation.check_POSTALCODE(lecturer.PostalCode)
    Datavalidation.check_CPHONE(lecturer.CPhone)
    Datavalidation.check_HPHONE(lecturer.HPhone)
    LCourseIDs = lecturer.LCourseIDs
    for i in LCourseIDs:
        if  not db.query(models.Course).filter(i == models.Course.cid).first():
            Validation.Errors["LCourseIDs"] = f"Course with ID {i} not found !"
    if len(Validation.Errors) != 0:
        return Validation.Errors
    return crud.create_lecturer(db = db, lecturer = lecturer)


# Read Lecturer
@router.get("/GetLE/{Lecturer_id}", response_model= schemas.Lecturer)
def read_lecturer(lecturer_id : int, db : Session = Depends(get_db)):

    db_lecturer = crud.get_lecture(db, lecturer_id = lecturer_id)
    if db_lecturer is None:
        raise HTTPException(status_code=404, detail="Lecturer Not Found !")
    return db_lecturer



# Delete Lecturer
@router.delete("/DeleteLE/{Lecturer_id}")
def delete_lecturer(lecturer_id: int, db: Session = Depends(get_db)):
    with Session(engine) as session:
        lecturer = session.get(models.Lecturer, lecturer_id)
        if not lecturer:
            raise HTTPException(status_code=404, detail="Lecturer not found")
        session.delete(lecturer)
        session.commit()
        return "deleted successfully!"
    


# Update Lecturer
@router.patch("/UpdateLE/{Lecturer_id}")
def update_lecturer(lecturer_lid : int, lecturer: schemas.LecturerUpdate, db:Session = Depends(get_db)):
    db_lecturer = crud.get_lecture(db, lecturer_id= lecturer_lid)
    if not lecturer_lid:
        raise HTTPException(status_code=404, detail="Lecturer not found")
    lecturer_data = lecturer.model_dump(exclude_unset= True)
    Validation.Errors = {}
    # Valid Data
    if "LID" in lecturer_data:
        Datavalidation.check_LID(lecturer_data["LID"])
    if "FName" in lecturer_data:
        Datavalidation.check_FNAME(lecturer_data["FName"])
    if "LName" in lecturer_data:
        Datavalidation.check_LNAME(lecturer_data["LName"])
    if "ID" in lecturer_data:
        Datavalidation.check_ID(lecturer_data["ID"])
    if "Department" in lecturer_data:
        Datavalidation.check_DEPARTMENT(lecturer_data["Department"])
    if "Major" in lecturer_data:
        Datavalidation.check_MAJOR(lecturer_data["Major"])
    if "Birth" in lecturer_data:
        Datavalidation.check_BIRTH(lecturer_data["Birth"])
    if "BornCity" in lecturer_data:
        Datavalidation.check_BornCity(lecturer_data["BornCity"])
    if "Address" in lecturer_data:
        Datavalidation.check_Address(lecturer_data["Address"])
    if "PostalCode" in lecturer_data:
        Datavalidation.check_POSTALCODE(lecturer_data["PostalCode"])
    if "CPhone" in lecturer_data:
        Datavalidation.check_CPHONE(lecturer_data["CPhone"])
    if "HPhone" in lecturer_data:
        Datavalidation.check_HPHONE(lecturer_data["HPhone"])
    if "LCourseIDs" in lecturer_data:
        LCourseIDs = lecturer.LCourseIDs
        for i in LCourseIDs:
            if not db.query(models.Course).filter(i == models.Course.cid).first():
                Validation.Errors["LCourseIDs"] = f"LCourse with CID {i} not found !"

    if len(Validation.Errors) != 0:
        return Validation.Errors
    
    for key, value in lecturer_data.items():
        setattr(db_lecturer, key, value)
    db.add(db_lecturer)
    db.commit()
    db.refresh(db_lecturer)
    return db_lecturer
