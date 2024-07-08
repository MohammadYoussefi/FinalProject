from database import Base
from sqlalchemy import Column, Integer, String, PickleType


class Course(Base):
    __tablename__ = "Courses"

    cid = Column(String, primary_key=True)
    CName = Column(String(10), nullable=True)
    Department = Column(String, nullable=True)
    Credit = Column(Integer, nullable=True)

    


class Student(Base):
    __tablename__ = "Students"

    STID = Column(Integer, primary_key=True)
    FName = Column(String(10), nullable=True)
    LName = Column(String(10), nullable=True)
    Father = Column(String(10), nullable=True)
    Birth = Column(String, nullable=True)
    IDS = Column(String, nullable=True)
    BornCity = Column(String, nullable=True)
    Address = Column(String(100), nullable=True)
    PostalCode = Column(Integer, nullable=True)
    CPhone = Column(String, nullable=True)
    HPhone = Column(String, nullable=True)
    Department = Column(String, nullable=True)
    Major = Column(String, nullable=True)
    Married = Column(String,nullable=True)
    ID = Column(String(10), nullable=True)
    SCourseIDs = Column(PickleType)
    LIDs = Column(PickleType)

    
class Lecturer(Base):
    __tablename__ = "Lecturers"

    LID = Column(String(6), primary_key=True)
    FName = Column(String(10), nullable=True)
    LName = Column(String(10), nullable=True)
    Birth = Column(String, nullable=True)
    BornCity = Column(String, nullable=True)
    Address = Column(String(100), nullable=True)
    PostalCode = Column(Integer, nullable=True)
    CPhone = Column(String, nullable=True)
    HPhone = Column(Integer, nullable=True)
    Department = Column(String, nullable=True)
    Major = Column(String, nullable=True)
    ID = Column(String(10), nullable=True)
    LCourseIDs = Column(PickleType)









