from .student import Student

class Teacher:
    def __init__(self , name:str , teacher_id:int , subject:str ):
        self.name = name
        self.id = teacher_id
        self.subject = subject
    
    def assign_marks(self, student: Student, subject: str, marks: int):
        return student.add_marks(subject, marks)

    def view_student(self, student:Student):
        return student.display_info()
        

    def update_marks(self, student:Student, subject:str , new_marks: int):
        return student.add_marks(subject, new_marks )

    def remove_marks(self, student: Student, subject: str):
        if subject in student.marks:
            del student.marks[subject]
            return f"Removed marks for {subject}."
        else:
            return f"{subject} not found in student's record."