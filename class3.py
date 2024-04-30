class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        total_marks = sum(self.marks)
        avg = total_marks / len(self.marks)
        print("Hi", self.name + ",", "your average score is:", avg)

s1 = Student("Tony Stark", [99, 98, 97])
s1.get_avg()
