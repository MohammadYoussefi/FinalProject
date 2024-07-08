from CourseMain import router as Course_router
from StudentMain import router as Student_router
from LecturerMain import router as Lecturer_router
from fastapi import FastAPI




app = FastAPI()

app.include_router(Course_router)
app.include_router(Student_router)
app.include_router(Lecturer_router)

