from app import db, Student, app

# Add Sample Data
with app.app_context():
    student1 = Student(id=1, name="Mohit Parshar", total_marks=85)
    student2 = Student(id=2, name="Dawid Warner", total_marks=92)
    student3 = Student(id=3, name="CR Ronaldo", total_marks=78)
    student4 = Student(id=4, name="Lionel Messi", total_marks=63)
    student5 = Student(id=5, name="MS Dhoni", total_marks=83)
    student6 = Student(id=6, name="Sanju Samson", total_marks=76)
    student7 = Student(id=7, name="Travis Head", total_marks=95)
    student8 = Student(id=8, name="Roger Federer", total_marks=57)
    student9 = Student(id=9, name="Andy Murray", total_marks=72)
    student10 = Student(id=10, name="Rafel Nadal", total_marks=67)
    student11 = Student(id=11, name="Novack Djokovic", total_marks=88)
    student12 = Student(id=12, name="Rahul Dravid", total_marks=78)
    student13 = Student(id=13, name="Jos Buttler", total_marks=74)
    student14 = Student(id=14, name="Elon Musk", total_marks=81)
    student15 = Student(id=15, name="Alex Carry", total_marks=63)

    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(student4)
    db.session.add(student5)
    db.session.add(student6)
    db.session.add(student7)
    db.session.add(student8)
    db.session.add(student9)
    db.session.add(student10)
    db.session.add(student11)
    db.session.add(student12)
    db.session.add(student13)
    db.session.add(student14)
    db.session.add(student15)

    db.session.commit()

print("Sample data added!")
