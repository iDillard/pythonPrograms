# Student Module for the group project
# Author: Isaiah Dillard
# Date: 4/18/2022
# This module gathers and processes student information for the main program
# built within registration.py

def main():

    student_list = [('1001', '111'),
                    ('1002', '222'),
                    ('1003', '333'),
                    ('1004', '444')]

    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}

    course_hours = {'CSC101': 3,
                    'CSC102': 4,
                    'CSC103': 5,
                    'CSC104': 3}

    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': ['1004']}

    course_max_size = {'CSC101': 3,
                       'CSC102': 2,
                       'CSC103': 1,
                       'CSC104': 3}

    # student_id = input('Enter Student id: ')

    # add_course(student_id, course_roster, course_max_size)
    # drop_course(student_id, course_roster)
    # list_courses(student_id, course_roster)

def add_course(id, c_roster, c_max_size):

    # test if the desired course is an existing course
    while True:
        desired_course = input('Enter course you want to add: ')
        if desired_course not in c_roster:
            print('Course not found')
            print()
            break
        elif id in c_roster[desired_course]:
            print('You are already enrolled in this course.')
            print()
            break
        elif len(c_roster[desired_course]) >= c_max_size[desired_course]:
            print('Course already full')
            print()
            break
        else:
            c_roster[desired_course].append(id)
            print(f'Course added')
            print()
            break


def drop_course(id, c_roster):

    while True:
        dropped = input('Enter course you want to drop: ')
        if dropped not in c_roster:
            print('Course not found')
            print()
            break
        elif id not in c_roster[dropped]:
            print('You are not enrolled in that course')
            print()
            break
        else:
            c_roster[dropped].remove(id)
            print('Course dropped')
            print()
            break


def list_courses(id, c_roster):
    course_list = []

    while True:
        course_count = 0
        for course in c_roster:
            if id in c_roster[course]:
                course_list.append(course)
                course_count += 1


        for i in course_list:
            print(i)

        print(f'Total number: {course_count}')
        print()
        break

main()
