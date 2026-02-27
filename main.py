class Student:
    def __init__(self, name, student_id, department, classroom, birthday, age, email):
        self.name = name
        self.student_id = student_id
        self.department = department
        self.classroom = classroom
        self.birthday = birthday
        self.age = age
        self.email = email

    def show_profile(self):
        print("===== Student Profile =====")
        print(f"ชื่อ: {self.name}")
        print(f"รหัสนักศึกษา: {self.student_id}")
        print(f"สาขา: {self.department}")
        print(f"ชั้นเรียน: {self.classroom}")
        print(f"วันเกิด: {self.birthday}")
        print(f"อายุ: {self.age}")
        print(f"อีเมล: {self.email}")
        print("===========================")


# นักเรียนคนที่ 1
student1 = Student(
    "Krich", "66202040120", "เทคโนโลยีธุรกิจดิจิทัล",
    "ปวช.3/1", "17 เมษายน 2008", 17, "66202040120@svc.ac.th"
)

# นักเรียนคนที่ 2
student2 = Student(
    "Nattapon", "66202040095", "เทคโนโลยีธุรกิจดิจิทัล",
    "ปวช.3/1", "14 มีนาคม 2008", 17, "66202040095@svc.ac.th"
)

# นักเรียนคนที่ 3
student3 = Student(
    "Bat", "66202040101", "เทคโนโลยีธุรกิจดิจิทัล",
    "ปวช.3/3", "10 เมษายน 2007", 18, "66202040101@svc.ac.th"
)

# นักเรียนคนที่ 4
student4 = Student(
    "Anan", "66202040123", "เทคโนโลยีธุรกิจดิจิทัล",
    "ปวช.3/1", "12 กุมภาพันธ์ 2008", 17, "66202040123@svc.ac.th"
)

# นักเรียนคนที่ 5
student5 = Student(
    "Kittipong", "66202040124", "คอมพิวเตอร์ธุรกิจ",
    "ปวช.3/2", "30 มีนาคม 2007", 18, "66202040124@svc.ac.th"
)

# นักเรียนคนที่ 6
student6 = Student(
    "Pongsak", "66202040125", "เทคโนโลยีธุรกิจดิจิทัล",
    "ปวช.3/1", "8 สิงหาคม 2008", 17, "66202040125@svc.ac.th"
)

# นักเรียนคนที่ 7
student7 = Student(
    "Chayut", "66202040126", "คอมพิวเตอร์ธุรกิจ",
    "ปวช.3/2", "14 กันยายน 2007", 18, "66202040126@svc.ac.th"
)

# นักเรียนคนที่ 8
student8 = Student(
    "Teerapat", "66202040127", "เทคโนโลยีธุรกิจดิจิทัล",
    "ปวช.3/1", "22 พฤศจิกายน 2008", 17, "66202040127@svc.ac.th"
)

# นักเรียนคนที่ 9
student9 = Student(
    "Surasak", "66202040128", "คอมพิวเตอร์ธุรกิจ",
    "ปวช.3/2", "3 ธันวาคม 2007", 18, "66202040128@svc.ac.th"
)

# นักเรียนคนที่ 10
student9 = Student(
    "Surasak", "66202040128", "คอมพิวเตอร์ธุรกิจ",
    "ปวช.3/2", "3 ธันวาคม 2007", 18, "66202040128@svc.ac.th"
)

# นักเรียนคนที่ 11
student9 = Student(
    "Surasak", "66202040128", "คอมพิวเตอร์ธุรกิจ",
    "ปวช.3/2", "3 ธันวาคม 2007", 18, "66202040128@svc.ac.th"
)

# นักเรียนคนที่ 12
student9 = Student(
    "Surasak", "66202040128", "คอมพิวเตอร์ธุรกิจ",
    "ปวช.3/2", "3 ธันวาคม 2007", 18, "66202040128@svc.ac.th"
)
# รวมเป็นกลุ่ม
students = [
    student1, student2, student3,
    student4, student5, student6,
    student7, student8, student9
]

# แสดงข้อมูลนักเรียนทุกคน
for s in students:
    s.show_profile()
