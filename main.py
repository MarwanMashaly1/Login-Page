"""
Marwan Mashaly
Dec 9, 2020
Assignment 9.3
"""
#-------------------Imports-------------------------
import turtle       # allows to use the turtle library
import time         # allows to use the time module

#-------------------Treen Screen------------------------
wn = turtle.Screen()                   # Create a graphics window
wn.bgcolor("light grey")               # set the background color
wn.window_width()                   # set width for screen 
wn.window_height()                  # set height for screen
tia = turtle.Turtle()                  # tia
tia.speed(5)                           # set tia speed to 0
style = ("Arial", 17)               # set style
#--------------------Functions-----------------------
strRun = "yes"          # set value

def drawButtons():      # function to draw buttons
    for i in range(4):  # range for square
        tia.fd(100)     # forward
        tia.rt(90)      # right 90
    tia.pu()            # pen up
    tia.goto(10,-60)    # 10, -60
    tia.pd()            # pen down
    tia.write("Login", font=style)  # write
    tia.pu()            # pen up
    tia.goto(0, 200)    # 0, 200
    tia.pd()            # pen down

    for j in range(4):  # range for square
        tia.fd(100)     # forward
        tia.rt(90)      # right 90
    tia.pu()            # pen up
    tia.goto(10,140)    # 10, 140
    tia.pd()            # pen down
    tia.write("Sign Up", font=style)    # write on screen

def choices(intChoice):         # function to choose 
    print("Please Click on what you would like to do.") # print
    if intChoice == 1:          # if choice = 1
        getdetails()            # call function
    elif intChoice == 2:        # if choice = 2
        checkdetails()          # call function

def getdetails():               # function to sign up
    print("Please Provide sign")        # print
    name = str(input("Name: "))         # get input
    password = str(input("Password: ")) # get input
    file = open("User_Data.txt",'r')    # open file
    info = file.read()      # read file
    if name in info:    # condition if found
        return "Name Unavailable. Please Try Again" # return
    file.close          # close file
    file = open("User_Data.txt",'w')    # open file
    info = info + " " +name + "\n" + " " + password + "\n"
    file.write(info)    # write to file
    file.close          # close file
    tia.clear()         # clear tia
    tia.pu()            # pen up
    tia.goto(-180, 0)   # -180, 0
    tia.write("Signed up Succesfily", font=("Arial", 25))   # write on screen
    time.sleep(3)       # sleep for 3 seconds
    tia.clear()         # clear screen
    tia.write("Main page Loading", font=("Arial", 25))  # write on screen
    time.sleep(3)       # sleep for 3 seconds
    tia.clear()         # clear screen
    mainPage()          # call function

def checkdetails():     # function for login
    print("Please Provide info ")       # print
    name = str(input("Name: "))         # get input
    password = str(input("Password: ")) # get input
    file = open("User_Data.txt",'r')    # open file
    info = file.read()          # read file 
    info = info.split()         # split lines
    if name in info:           # condition if found
        index = info.index(name) + 1    # set value
        usrPassword = info[index]       # set value 
        if usrPassword == password:            #condition if true
            print("Welcome Back, " + name)      # print
        else:       # else
            return "Password entered is wrong"      # return
    else:           # else
        return "Name not found. Please Sign Up."    # return
    tia.clear()         # clear tia
    tia.pu()            # pen up
    tia.goto(-180, 0)   # -180, 0
    tia.write("Login Succesfily", font=("Arial", 25))   # write on screen
    time.sleep(3)       # sleep for 3 seconds
    tia.clear           # clear
    tia.write("Main page Loading", font=("Arial", 25))  # write on screen
    time.sleep(3)       # sleep for 3 seconds
    tia.clear()         # clear screen
    mainPage()          # call function 

def clickButton(x,y):   # function to click in choice
    print(x,y)          # print
    SignupPressCordX = range(0, 100)    # set range
    SignupPressCordY = range(100, 200)  # set range
    loginPressCordX = range(0, 100)     # set range
    loginPressCordY = range(-100, 0)    # set range
    if int(x) in SignupPressCordX and int(y) in SignupPressCordY:       # condition if in range
        intChoice = 1       # set value to variable
    if int(x) in loginPressCordX and int(y) in loginPressCordY:         # condition if in range
        intChoice = 2       # set value to variable
    choices(intChoice)      # call function

def mainPage():             # function to draw on main
    tia.pu()                # pen up
    tia.goto(-50, 0)        # -50, 0
    tia.pd()                # pen down
    for i in range(4):      # range for square
        tia.fd(100)         # forward 100
        tia.lt(90)          # right 90
    tia.fd(50)              # forward
    tia.circle(50)          # draw circle
    tia.rt(90)              # right 90
    tia.pu()                # pen up
    tia.fd(20)              # forward
    tia.lt(135)             # left 135
    tia.pd()                #pen down
    for j in range(4):      # range for dquare
        tia.fd(100)         # forward 
        tia.lt(90)          # right 90
    tia.rt(135)         # right 135
    tia.fd(150)         # forward 150
    tia.lt(90)          # left 90
    tia.fd(200)         # forward
    tia.rt(180)         # turn right 180
    tia.fd(400)         # forward 
#---------------------Main---------------------------
drawButtons()               # call functiom
while strRun == "yes":      # loop while = yes
    wn.onclick(clickButton)
    wn.listen()
    wn.mainloop()