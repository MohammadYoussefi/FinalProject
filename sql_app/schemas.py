from pydantic import BaseModel
from typing import Any, Optional
import typing




class Course(BaseModel):
    cid : str
    CName : str
    Department : str
    Credit : int
    
    class Config:
        orm_mode = True

class CourseUpdate(BaseModel):
    CName : str | None = None
    Department : str | None = None
    Credit : int | None = None

# ---------------------------------------------------

class Student(BaseModel):
    STID : int
    FName : str
    LName : str
    Father : str
    Birth : str = "0000/00/00"
    IDS : str
    BornCity : str
    Address : str
    PostalCode : int
    CPhone : str
    HPhone : int
    Department : str
    Major : str
    Married : str
    ID : str
    SCourseIDs : Any  = []
    LIDs : Any = []

    class Config:
        orm_mode = True

class StudentUpdate(BaseModel):
    FName : Optional[str] = None
    LName : Optional[str] = None
    Father : Optional[str] = None
    Birth : Optional[str] = None
    IDS : Optional[str] = None
    BornCity : Optional[str] = None
    Address : Optional[str] = None
    PostalCode : Optional[int] = None
    CPhone : Optional[str] = None
    HPhone : Optional[int] = None
    Department : Optional[str] = None
    Major : Optional[str] = None
    Married : Optional[str] = None
    ID : Optional[str] = None
    SCourseIDs : Optional[Any] = []
    LIDs : Optional[Any] = []

# # ---------------------------------------
class Lecturer(BaseModel):
    LID : str
    FName : str
    LName : str
    ID : str
    Department : str
    Major : str
    Birth : str = "0000/00/00"
    BornCity : str
    Address : str
    PostalCode : int
    CPhone : str
    HPhone : int
    LCourseIDs : Any = []
    class Config:
        orm_mode = True

class LecturerUpdate(BaseModel):
    FName : Optional[str] = None
    LName : Optional[str] = None
    ID : Optional[str] = None
    Department : Optional[str] = None
    Major : Optional[str] = None
    Birth : Optional[str] = "0000/00/00" 
    BornCity : Optional[str] = None
    Address : Optional[str] = None
    PostalCode : Optional[int] = None
    CPhone : Optional[str] = None
    HPhone : Optional[int] = None
    LCourseIDs : Optional[Any] = []
