from .student import Student
from .teacher import Teacher

class ReportCard:
    def __init__(self, student: Student, teacher:Teacher):
        self.student = student
        self.teacher = teacher

    def generate_report(self):
        self.student.display_info()
        self.student.val_average()
        self.student.get_grade()
