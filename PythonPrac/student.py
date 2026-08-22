
#  Student: Rahul | Roll: 101 | Average: 85.0 | Grade: B

class Student:

    def __init__(self,name, roll_no, marks):
        self.name = name 
        self.roll_no = roll_no
        self.marks = marks

    def average(self):
        return sum(self.marks)/len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"

        elif avg >= 75:
            return "B"

        elif avg >= 60:
            return "C"
        else:
            return "D"

    def __str__(self):
        return (f"Student Name : {self.name} | "
                f"Roll No : {self.roll_no} | "
                f"Average : {self.average()} |"
                f"Grade : {self.grade()}"
                )


s1 = Student("Hari Krishna",365,[90,56,87])
s2 = Student("Hari Krishna Tanna",366,[99,66,77])

print(s1)
print(s2)
print(s1.grade())