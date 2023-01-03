# ----------------------------------------------------------------
# Author: Samuel Martinez Sanchez
# Date:  4/18/2022
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
def main():
    # student_list = [('1001', '111'), ('1002', '222'),
    #                 ('1003', '333'), ('1004', '444')]
    student_in_state = {'1001': True, '1002': False,
                        '1003': True, '1004': False}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002', "1003"],
                     'CSC104': []}



def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function calculate billing information. It takes four
    # parameters: id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # This function returns the number of course hours and tuition
    # cost.
    # ------------------------------------------------------------
    # Checks to see if studentID is in state or out of state
    hours = 0
    if s_in_state[id] == True:
        # print(f"I am in state {id}")
        # Loops through c_roster |This checks to see where the student is in the course
        for course, value in c_rosters.items():
            for loop_id in value:
                if id == loop_id:
                    # print(f" {id} is in this class {course}")

                    # Loops through c_hours
                    for h_course, h_hours in c_hours.items():
                        # print(f"{h_course} class with {h_hours} hours")
                        if course == h_course:
                            hours += c_hours[course]
                            cost = hours * 225


        # print(f"Total Hours: {hours} and Total: {cost}")


    elif s_in_state[id] == False:

        # print(f"I am OUT of state {id}")
        # Loops through c_roster |This checks to see where the student is in the course
        for course, value in c_rosters.items():
            for loop_id in value:
                if id == loop_id:
                    # print(f" {id} is in this class {course}")

                    # Loops through c_hours
                    for h_course, h_hours in c_hours.items():
                        # print(f"{h_course} class with {h_hours} hours")
                        if course == h_course:
                            hours += c_hours[course]
                            cost = hours * 850

        # print(f"Total Hours: {hours} and Total: {cost}")
    #
    # else:
    #     print(f"Student does not exits In state or Out of state")

    display_hours_and_bill(hours,cost)




def display_hours_and_bill(hours, cost):
    # ------------------------------------------------------------
    # This function prints the number of course hours the student
    # is taking and the total tuition cost. It takes two parameters:
    # hours and cost. This function has no return value.
    # ------------------------------------------------------------
    pass  # temporarily avoid empty function definition

    print(f"Course load {hours} credit hours")
    print(f"Enrollment cost: ${cost:.2f}")
    print()

main()
