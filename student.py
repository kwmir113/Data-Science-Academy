class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  def get_grade(self):
    return self.grade

s1 = Student("Tim", 19, 90)
s2 = Student("Susan", 18, 92)
s3 = Student("Kam", 25, 63)
print (s1.name, s1.age, s1.grade)
print (s2.name, s2.age, s2.grade)
print (s3.name, s3.age, s3.grade)
