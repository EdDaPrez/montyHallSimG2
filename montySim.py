print("Monte Hall Simulation \n")
print("You are a participant in a gameshow and are presented with 3 doors by the host.\nBehind one door, there is a brand new car. But")

import time
import random

counter = 0 #counts the amount of processes
finalTime = 0
swapCar = 0
noSwapCar = 0

initialTime = time.perf_counter()
while (finalTime-initialTime < 60):
    doorChoice = random.randint(0,2)
    x=0
    while x > 1:
        firstChoice = random.randint(0,2)
        if firstChoice != doorChoice:
            x = 1
    secondChoice = random.randint(0,2)
    while x > 2:
        secondChoice = random.randint(0,2)
        if secondChoice != firstChoice:
            x = 2
    if (secondChoice != doorChoice):
        swapCar = swapCar + 1
    else:
        noSwapCar = noSwapCar + 1
    counter = counter + 1
    finalTime = time.perf_counter()
print(str(counter) + " total iterations")
print(str(swapCar) + " cars earned after swapping doors")
print(str(noSwapCar) + " cars earned without swapping doors")
