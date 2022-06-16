#INITIALIZE
#import libraries
import time
import random

#define variables
totalCounter = 0 
finalTime = 0 
swapDoor = 0 #keeps count of the amount of cars earned after swapping doors
noSwapDoor = 0 #keeps count of the amount of cars earned without swapping doors

#define functions
def hostChoice():
    hostOptionList = []
    for i in range(1, 4):
        if i != carDoor and i != initialUserChoice:
            hostOptionList.append(i)
    return random.choice(hostOptionList)

#RUN
#make sure program is running
print("Monty Hall Simulation \n")
print("Wait 60 seconds...")
initialTime = time.perf_counter()
while (finalTime-initialTime < 5): #loop ends when 1 minute reached
    carDoor = random.randint(1,3)#random door car is behind
    initialUserChoice = random.randint(1,3)#random door user chooses
    userOptions = [1, 2, 3]
    userOptions.remove(hostChoice())
    secondChoice = random.choice(userOptions)
    if secondChoice == initialUserChoice and carDoor == secondChoice:
        noSwapDoor = noSwapDoor + 1 
    elif secondChoice != initialUserChoice and carDoor == secondChoice:
        swapDoor = swapDoor + 1
    totalCounter = totalCounter + 1 #keeps count of the iteration of the loop
    finalTime = time.perf_counter() #time that loop uses to determine whether to terminate or not
print(str(totalCounter) + " total iterations")
print(str(swapDoor) + " times won after swapping doors. Won ", str((swapDoor/(swapDoor + noSwapDoor)) * 100), "% of the time.")
print(str(noSwapDoor) + " times won without swapping doors. Won ", str((noSwapDoor/(swapDoor + noSwapDoor)) * 100), "% of the time.")
