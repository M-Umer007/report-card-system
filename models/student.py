class Student:
    def __init__(self , name:str , age:int , student_id:int ):
        self.name = name
        self.age = age
        self.id = student_id
        self.marks = {}


    def add_marks(self, subject:str,marks:int):
        self.marks[subject] = marks

    
    def val_average(self):
        marks = self.marks.values()
        lenOfSubjects = len(self.marks)
        avg = sum(marks)/lenOfSubjects
        return avg
    
    def get_grade(self):
        avg = self.val_average()
        if avg is None:
            return "No marks added"
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        elif avg >= 40:
            return "E"
        else:
            return "F"
        
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.id}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")