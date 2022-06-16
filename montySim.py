print("Monty Hall Simulation \n")
print("Wait 60 seconds...")

import time
import random

totalCounter = 0 #keeps count of the iteration of the loop
finalTime = 0 #time that loop uses to determine whether to terminate or not
swapDoor = 0 #keeps count of the amount of cars earned after swapping doors
noSwapDoor = 0 #keeps count of the amount of cars earned without swapping doors
secondChoice = 0 #global variable created to be referenced within the loop
userSecondChoice = 0
carDoor = 0
initialUserChoice = 0
firstChoice = 0
secondChoice = 0
indexCount = 0

initialTime = time.perf_counter()
while (finalTime-initialTime < 60):
    carDoor = random.randint(1,3)#random door car is behind
    initialUserChoice = random.randint(1,3)#random door user chooses
    hostOptionList = [] 
    for i in range(1, 4):
        if i != carDoor and i != initialUserChoice:
            hostOptionList.append(i)
    hostChoice = random.choice(hostOptionList)
    userOptions = [1, 2, 3]
    userOptions.remove(hostChoice)
    secondChoice = random.choice(userOptions)
    if secondChoice == initialUserChoice and carDoor == secondChoice:
        noSwapDoor = noSwapDoor + 1 
    elif secondChoice != initialUserChoice and carDoor == secondChoice:
        swapDoor = swapDoor + 1
    totalCounter = totalCounter + 1
    finalTime = time.perf_counter()
print(str(totalCounter) + " total iterations")
print(str(swapDoor) + " times won after swapping doors. Won ", str((swapDoor/(swapDoor + noSwapDoor)) * 100), "% of the time.")
print(str(noSwapDoor) + " times won without swapping doors. Won ", str((noSwapDoor/(swapDoor + noSwapDoor)) * 100), "% of the time.")
