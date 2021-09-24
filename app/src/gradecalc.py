# Create a function called: calculate_avg_grade
# Parameters: the function should receive 1 parameter: a list of student objects
#             Remember a list can contain duplicates, so you can expect two student objects with same ID but different grades
# Returns: the function should return a dictionary with student ID as key and student average grade as value
#
# Example:
# input: [Student('s1',20,1824,90.5), Student('s2',21,1823,80.0), Student('s1',20,1824,70.0)]
# output: { 1824: 80.25, 1823: 80.0 }
#
# If the list of students is empty, return an empty dictionary
# Make sure that you add type hints to the function paramter and return value

from app.src.Student import Student
from app.src.utils import calculate_avg


def calculate_avg_grade(student: list[Student]) ->dict[int, float]:
    #stu_grades=dict[int, list[Student]]
    stu_grades={}
    for students in student:
        stu_id: int = students.id
        if stu_id in stu_grades.keys():
            stu_grades.get(stu_id).append(students.grade)
        else:
            stu_grades[stu_id]=[students.grade]

    #avg_grades=dict[int, float]
    avg_grades={}
    for stu, grades in stu_grades.items():
        avg_grades[stu]=calculate_avg(grades)

    return avg_grades