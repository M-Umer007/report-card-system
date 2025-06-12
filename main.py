from models.student import Student
from models.teacher import Teacher
from models.report_card import ReportCard

t = Teacher("UmerTeacher", 1122, "English")
s = Student("UmerStudent", 17, 33444)
r = ReportCard(s, t)

t.assign_marks(s,"English", 77)
t.assign_marks(s,"Computer", 83)
t.assign_marks(s,"PST", 74)
t.assign_marks(s,"Physics", 70)
t.assign_marks(s,"Mathematics", 45)

r.generate_report(s)
