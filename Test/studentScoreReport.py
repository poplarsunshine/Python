names = input("for Example:jack,tony Enter names:" ).title().split(",")
assignments = input("for Example:5,3 Enter assignments:").title().split(",")
grades = input("for Example:65,83 Enter grades:").title().split(",")

message = """
Hi {},

This is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date.
"""

for index in range(len(names)):
    name = names[index]
    miss_assignment = assignments[index]
    current_grade = grades[index]
    potential_grade = miss_assignment * 2 + current_grade
    print(message.format(name, miss_assignment, current_grade, potential_grade))

print("-------------")

for name, miss_assignment, current_grade in zip(names, assignments, grades):
    potential_grade = miss_assignment * 2 + current_grade
    print(message.format(name, miss_assignment, current_grade, potential_grade))
