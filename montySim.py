#INITIALIZE
#import libraries
import time
import random

#define variables
totalCounter = 0 
finalTime = 0 
swapDoorW = 0 #keeps count of the amount of cars earned after swapping doors
swapDoorL = 0
noSwapDoorW = 0 #keeps count of the amount of cars earned without swapping doors
noSwapDoorL = 0

#define functions
def hostChoice():
    hostOptionList = []
    for i in range(1, 4):
        if i != carDoor and i != initialUserChoice:
            hostOptionList.append(i)
    return random.choice(hostOptionList)

#RUN
#print to make sure program is running
print("Monty Hall Simulation \n")
print("Wait 60 seconds...\n")
progStartTime = time.perf_counter()
while (finalTime-progStartTime < 60): #loop ends when 1 minute reached
    carDoor = random.randint(1,3)#random door car is behind
    initialUserChoice = random.randint(1,3)#user chooses random door
    secondChoiceOptions = [1, 2, 3]
    secondChoiceOptions.remove(hostChoice())
    secondChoice = random.choice(secondChoiceOptions)#makes user's second choice
    if secondChoice == initialUserChoice:
        if carDoor == secondChoice:
            noSwapDoorW = noSwapDoorW + 1 
        else:
            noSwapDoorL = noSwapDoorL + 1
    else:
        if carDoor == secondChoice:
            swapDoorW = swapDoorW + 1
        else:
            swapDoorL = swapDoorL + 1
    totalCounter = totalCounter + 1 #keeps count of the iteration of the loop
    finalTime = time.perf_counter() #time that loop uses to determine whether to terminate or not
print(str(totalCounter) + " total iterations")
print(str(swapDoorW) + " times won after swapping doors.", str((swapDoorW/(swapDoorW+swapDoorL)) * 100), "% chance of winning if you switch.")
print(str(noSwapDoorW) + " times won without swapping doors.", str((noSwapDoorW/(noSwapDoorW+noSwapDoorL)) * 100), "% chance of winning if you switch.")
