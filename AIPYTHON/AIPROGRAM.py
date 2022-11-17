#ai program
import os
import time
import subprocess
import optparse
import re
import site


#login and welcome system
print("")
print("")
print("Hello")
print("Please Login")
print("")
print("")
UserName = input ("Enter Username: ")
print("")
PassWord = input ("Enter Password: ")
if UserName == 'Blake' and PassWord == '2433':
    print("")
    print ("Login successful!")
    time.sleep(2)
else:
    print("Nice try")
    time.sleep(2)
    os.system("shutdown /s /t 1")
     
        
#ask how doing and mac address changer  
print("")
print("Hello, Blake Weiss")
print("Welcome Back")
print("")
print("How are you today")
welcomecommand = input("Im doing :" )
print("Great to hear your doing " + welcomecommand + " today.")
print("")    
print("May I suggest changing your mac address")
print("If your intrested in doing this press 1 and it will be on your to do list")
mac_addressgoal = input("Type 1 for the goal to be entered into your list. Type 2 for it not to be entered:")
if mac_addressgoal == "1":
    print("")
    print("")
    goaladdr = ("Change Mac Address")
    print(goaladdr)
if mac_addressgoal == "2":
    print("")
    print("")
    print("Well even if you dont want to change it you still have to make your goals list")
    


#goals list
print("What are todays goals")
goalscommandone = input("1st goal :")
goalscommandtwo = input("2nd goal :")
goalscommandthree = input("3rd goal :")
list_file = open("goalslist.txt","w")
list_file.write('goals!\n')
list_file.write(goalscommandone)
list_file.write(goalscommandtwo)
list_file.write(goalscommandthree)
list_file.close()



#toolkit starter
print("Blake would you like to start your toolkit of hacking tools")
toolkitintro = input("if you want to start it enter 1 if not close the ai program: " )
if toolkitintro == "1":
    print("Hello, Blake I am starting the toolkit for you")
    time.sleep(1)
    print("")
    print("Starting up")
    time.sleep(1)
    print("")
    print("")
    print("Would you like for me to start your toolkit type start to start it")
    toolkitstart = input("Your choice here: ")
    time.sleep(1)
if toolkitstart == "start":
    print("Please choose which tool you would like")
    print("Press 1 for DDOS")
    print("Press 2 for PINGER")
    print("Press 3 for VPN")
    print("99 to exit program")
    toolkitone = input("Choose which tool you want to use:" )
if toolkitone == "1":
    time.sleep(1)
    print("DDOS starting up")
    import REAPER_DDOS.py
    os.system('python REAPER_DDOS.py')

if toolkitone == "2":
    time.sleep(1)
    print("PINGER starting up")
    subprocess.call([r'C:\Users\Blake Weiss\OneDrive\Desktop\AIPYTHON\grim_reaper_bjw.bat'])
    
if toolkitone == "3":
    time.sleep(1)
    print("VPN starting up")


if toolkitone == "99":
    time.sleep(1)
    print("Shutdown")
    exit()

