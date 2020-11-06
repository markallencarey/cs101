print ("Hello world")

grade = int(input("What was your score: "))
letterGrade = ""

if grade >= 93:
  letterGrade = "A"
elif grade >= 90:
  letterGrade = "A-"
elif grade >= 87:
  letterGrade = "B+"
elif grade >= 83:
  letterGrade = "B"
elif grade >= 80:
  letterGrade = "B-"
elif grade >= 77:
  letterGrade = "C+"
elif grade >= 73:
  letterGrade = "C"
elif grade >= 70:
  letterGrade = "C-"
elif grade >= 67:
  letterGrade = "D+"
elif grade >= 63:
  letterGrade = "D"
elif grade >= 60:
  letterGrade = "D-"
else:
  letterGrade = "F"
  
print ("For a score of " + str(grade) + ", your grade is a " + letterGrade + ".")