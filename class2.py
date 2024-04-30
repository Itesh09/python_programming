#create class and print the average 
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks





    def avg(self):
        sum=0
        for val in self.marks:  
            sum+=val
        print("the average is ",sum/3)
    
student1=student("Ram",[10,22,33])
student1.avg()