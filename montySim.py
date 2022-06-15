print("Monty Hall Simulation \n")
print("You are a participant in a gameshow and are presented with 3 doors by the host.\nBehind one door, there is a brand new car. But")

import time
import random

counter = 0 #keeps count of the iteration of the loop
finalTime = 0 #time that loop uses to determine whether to terminate or not
swapDoor = 0 #keeps count of the amount of cars earned after swapping doors
noSwapDoor = 0 #keeps count of the amount of cars earned without swapping doors
secondChoice = 0 #global variable created to be referenced within the loop

initialTime = time.perf_counter()
while (finalTime-initialTime < 5):
    doorList = [0,1,2]
    carChoice = random.randint(0,2)
    doorList.remove(carChoice)
    userChoice = random.randint(0,2)
    if userChoice != carChoice:
        doorList.remove(userChoice)
    firstChoice = random.choice(doorList)
    secondChoice = random.randint(0,1)#0 is to swap, 1 is not to swap
    if userChoice != carChoice:
        swapDoor = swapDoor + 1
    else:
        noSwapDoor = noSwapDoor + 1
    counter = counter + 1
    finalTime = time.perf_counter()
print(str(counter) + " total iterations")
print(str(swapDoor) + " cars could be earned after swapping doors")
print(str(noSwapDoor) + " cars could be earned without swapping doors")
