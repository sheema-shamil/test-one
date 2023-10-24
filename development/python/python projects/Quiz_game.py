print("welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit() 

print("Okay let's play :) ")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('correct!')
else:
    print("incorrect!")


answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print('correct!')
else:
    print("incorrect!")


answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('correct!')
else:
    print("incorrect!")


answer = input("What does PSU stand for? ")
if answer == "power supply":
    print('correct!')
else:
    print("incorrect!")


answer = input("What does ROM stand for? ")
if answer == "read-only memory":
    print('correct!')
else:
    print("incorrect!")