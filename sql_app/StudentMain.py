from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import schemas, models, crud
from Validation import Datavalidation
import Validation


router = APIRouter(tags= ["Student"])

models.Base.metadata.create_all(bind = engine)
app = FastAPI()


def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()


# Create Students
@router.post("/CreateSTU/")
def create_Student(student: schemas.Student, db: Session = Depends(get_db)):
    if db.query(models.Student).filter(models.Student.STID == student.STID).first():
        raise HTTPException(status_code=409, detail="Student Number already exists")
    # Valid Data
    Validation.Errors = {}
    Datavalidation.check_STID(student.STID)
    Datavalidation.check_FNAME(student.FName)
    Datavalidation.check_LNAME(student.LName)
    Datavalidation.check_FATHER(student.Father)
    Datavalidation.check_BIRTH(student.Birth)
    Datavalidation.check_IDS(student.IDS)
    Datavalidation.check_BornCity(student.BornCity)
    Datavalidation.check_Address(student.Address)
    Datavalidation.check_POSTALCODE(student.PostalCode)
    Datavalidation.check_CPHONE(student.CPhone)
    Datavalidation.check_HPHONE(student.HPhone)
    Datavalidation.check_DEPARTMENT(student.Department)
    Datavalidation.check_MAJOR(student.Major)
    Datavalidation.check_MARRIED(student.Married)
    Datavalidation.check_ID(student.ID)

    SCourseIDs = student.SCourseIDs
    for i in SCourseIDs:
        if  not db.query(models.Course).filter(i == models.Course.cid).first():
            Validation.Errors["SCourseIDs"] = f"Course with ID {i} not found !"
    LIDs = student.LIDs
    for i in LIDs:
        if not db.query(models.Lecturer).filter(i == models.Lecturer.LID).first():
            Validation.Errors["LIDs"] = f"LID with ID {i} not found !"

    if len(Validation.Errors) != 0:
        return Validation.Errors
    
    return crud.create_student(db = db, student = student)



# Read Student
@router.get("/GetSTU/{student_id}", response_model= schemas.Student)
def read_student(student_id : int, db : Session = Depends(get_db)):

    db_student = crud.get_student(db, student_id = student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student Not Found !")
    return db_student


# Delete Student
@router.delete("/DeleteSTU/{Student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    with Session(engine) as session:
        student = session.get(models.Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student Not Found !")
        session.delete(student)
        session.commit()
        return "deleted successfully!"

# Update Student
@router.patch("/UpdateSTU/{student_STID}", response_model= schemas.Student)
def update_student(student_STID : int, student: schemas.StudentUpdate, db:Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id = student_STID)
    if not student_STID:
        raise HTTPException(status_code=404, detail="Student Not Found !")
    student_data = student.model_dump(exclude_unset= True)

    # Valid Data
    if "FName" in student_data:
        Datavalidation.check_FNAME(student_data["FName"])
    if "LName" in student_data:
        Datavalidation.check_LName(student_data["LName"])
    if "Father" in student_data:
        Datavalidation.check_FATHER(student_data["Father"])
    if "Birth" in student_data:
        Datavalidation.check_BIRTH(student_data["Birth"])
    if "IDS" in student_data:
        Datavalidation.check_IDS(student_data["IDS"])
    if "BornCity" in student_data:
        Datavalidation.check_BornCity(student_data["BornCity"])
    if "Address" in student_data:
        Datavalidation.check_Address(student_data["Address"])
    if "PostalCode" in student_data:
        Datavalidation.check_POSTALCODE(student_data["PostalCode"])
    if "CPhone" in student_data:
        Datavalidation.check_CPHONE(student_data["CPhone"])
    if "HPhone" in student_data:
        Datavalidation.check_HPHONE(student_data["HPhone"])
    if "Department" in student_data:
        Datavalidation.check_DEPARTMENT(student_data["Department"])
    if "Major" in student_data:
        Datavalidation.check_MAJOR(student_data["Major"])
    if "Married" in student_data:
        Datavalidation.check_MARRIED(student_data["Married"])
    if "ID" in student_data:
        Datavalidation.check_ID(student_data["ID"])
    if "SCourseIDs" in student_data:
        SCourseIDs = student.SCourseIDs
        for i in SCourseIDs:
            if  not db.query(models.Course).filter(i == models.Course.cid).first():
                raise HTTPException(status_code=404, detail=f"Course with ID {i} not found !")
    if "LIDs" in student_data:
        LIDs = student.LIDs
        for i in LIDs:
            if not db.query(models.Lecturer).filter(i == models.Lecturer.LID).first():
                raise HTTPException(status_code=404, detail=f"LID with ID {i} not found !")
    for key, value in student_data.items():
        setattr(db_student, key, value)
        
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student