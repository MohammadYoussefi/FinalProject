from sqlalchemy.orm import Session
import models, schemas


# ------------------------------------------------------------------------------------------

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.cid == course_id).first()



def create_course(db: Session, course: schemas.Course):
    db_course = models.Course(cid = course.cid, CName = course.CName, Department = course.Department, Credit = course.Credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course



# -------------------------------------------------------------------------------------------

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.STID == student_id).first()


def create_student(db: Session, student: schemas.Student):
    db_student = models.Student(STID = student.STID, FName = student.FName, LName = student.LName, \
                                Father = student.Father, Birth = student.Birth, IDS = student.IDS, \
                                BornCity = student.BornCity, Address = student.Address, PostalCode = student.PostalCode, \
                                CPhone = student.CPhone, HPhone = student.HPhone, Department = student.Department, \
                                Major = student.Major, Married = student.Married, ID = student.ID, SCourseIDs = student.SCourseIDs, \
                                LIDs = student.LIDs)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


# ------------------------------------------------------------------------------------------------
def get_lecture(db: Session, lecturer_id :int):
        return db.query(models.Lecturer).filter(models.Lecturer.LID == lecturer_id).first()



def create_lecturer(db: Session, lecturer : schemas.Lecturer):
    db_lecturer = models.Lecturer(LID = lecturer.LID, FName = lecturer.FName, LName = lecturer.LName, \
                                 Birth = lecturer.Birth, \
                                BornCity = lecturer.BornCity, Address = lecturer.Address, PostalCode = lecturer.PostalCode, \
                                CPhone = lecturer.CPhone, HPhone = lecturer.HPhone, Department = lecturer.Department, \
                                Major = lecturer.Major, ID = lecturer.ID, \
                                LCourseIDs = lecturer.LCourseIDs)
    db.add(db_lecturer)
    db.commit()
    db.refresh(db_lecturer)
    return db_lecturer     