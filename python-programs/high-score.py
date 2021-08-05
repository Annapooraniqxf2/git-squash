"""
calcuate the highest score from the list
"""

def get_no_of_students():
    "Get the total number of students"
    student_count = input("Enter the number of students")
    print(f"The number of student {student_count}")

    return student_count


def get_students_score(number_of_students):
    "Get the score for all the students"
    student_score_list  = []
    for i in range(int(number_of_students)):
        student_score = input("Enter the student score")
        student_score_list.append(int(student_score))
    print(f'The student score list is {student_score_list}')

    return student_score_list

def find_max_from_list(student_score_list):
    "Finding the maximum from  the list"
    max = 0
    for each_score in student_score_list:
        if each_score > max:
            max = each_score
    print(f'The maximum value from the list is {max}')


#Program starts here
if __name__ == "__main__":
    number_of_students = get_no_of_students()
    student_score_list = get_students_score(number_of_students)
    find_max_from_list(student_score_list)