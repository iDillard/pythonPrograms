#
# Author: Tuesday Group (Sam Martinez, Isaiah Dillard)
# Date: 4/18/2022
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
#

import billing
import student


def main():
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, in_state_list, course
    # list, max class size list and roster list.  It uses a loop to
    # serve multiple students. Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.

    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]
    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': []}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

    student_id = input('Enter ID to log in, or 0 to quit: ')

    while student_id != '0':
        while login(student_id, student_list) == False:
            print('ID or PIN incorrect')
            print()
            student_id = input('Enter ID to log in, or 0 to quit: ')

        print('ID and PIN verified')
        print()

        answer = input('Enter 1 to add course, 2 to drop course, 3 to list course, 4 to show bill, 0 to exit: ')

        while True:
            if answer == '1':
                student.add_course(student_id, course_roster, course_max_size)
            elif answer == '2':
                student.drop_course(student_id, course_roster)
            elif answer == '3':
                student.list_courses(student_id, course_roster)
            elif answer == '4':
                billing.calculate_hours_and_bill(student_id, student_in_state, course_roster, course_hours)
            elif answer == '0':
                break
            else:
                print('Enter 1, 2, 3, 4, or 0')
            answer = input('Enter 1 to add course, 2 to drop course, 3 to list course, 4 to show bill, 0 to exit: ')
        student_id = input('Enter ID to log in, or 0 to quit: ')


def login(id, s_list):
    user_pin = input('Enter PIN: ')

    user_info = tuple((id, user_pin))

    if user_info in s_list:
        return True
    else:
        return False


main()
