# About
This program similates a student registering for class.
Each class that is offered has a a set amount of students that are allowed to be in the class.

- StudentID:    Pins:    Instate:    Classes:    Credit Hours: 
- 1001          111      T           CSC101       3               
- 1002          222      F           CSC102       4
- 1003          333      T           CSC103       5
- 1004          444      F           CSC104       3


Program will recognize which student you are logging in as.

The user will then be prompted to add a class, drop a class, show bill, or exit the program.
If add a class is selected the user will be asked what class they want to register for.
If the class does not exist it will let the user know that the class does not exist. 
If the class the student selected is full the program will notify them that the class is full.
If the calss student is already enrolled in the class the program will let them know that they are already enrolled in the class. 
If neither condition is true the student will be added to the class roster and count. 

If the user desires to be dropped from the class all the same criteria will be checked.
If the class does not exist it will let the user know.
If the user is not enrolled in that class it will let the student know they are not enrolled in the class.
If the user is enrolled in the class it will remove the user from the class, lower the number of students in the class, and let the user know they have been removed.


The program also allows for multiple users to run the program
Upon a user selecting to exit the program, the log in prompt will display again.
The program will remember any changes made by the previous user. 

The bill option will show how much the student owes the institute.
Each is assigned an boolean value of in-state.
Depending on if the student is instate will determine how much the student will pay in tution.
