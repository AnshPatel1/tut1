# when we input number 1, we turn the car right, 2 -> left, 3-> forward, 4-> reverse, 5-> stop. 6-> exit, 0 -> help
ver = 3.0

help_message = '''____HELP____
                    Press 1 to take a right turn
                    Press 2 to take a left turn
                    Press 3 to go forward
                    Press 4 to go backwards
                    Press 5 to stop
                    Press 6 to exit
                    __________________'''
escape = True
while escape:
    status = input('Please enter option: ')
    status = int(status)
    if status == 1:
        print("Car is turning right")
    elif status == 2:
        print("Car is turning left")
    elif status == 3:
        print("Car is moving forward")
    elif status == 4:
        print("Car is moving backwards")
    elif status == 5:
        print("Car stopped, brakes applied")
    elif status == 6:
        print("Thanks for playing! Have a nice day!")
        escape = False
    elif status == 0:
        print(help_message)
    else:
        print(" Invalid Option, press 0 for help!")
