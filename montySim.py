totalCounter = 0 #keeps count of the iteration of the loop
finalTime = 0 #time that loop uses to determine whether to terminate or not
swapDoorW = 0 #keeps count of the amount of cars earned after swapping doors
swapDoorL = 0
noSwapDoorW = 0 #keeps count of the amount of cars earned without swapping doors
noSwapDoorL = 0
secondChoice = 0 #global variable created to be referenced within the loop
userSecondChoice = 0
carDoor = 0
userChoice = 0
firstChoice = 0
secondChoice = 0
indexCount = 0

initialTime = time.perf_counter()
while (finalTime-initialTime < 5):
    carDoor = random.randint(1,3)
    userChoice = random.randint(1,3)
    hostOptionList = []
    indexCount = 0
    for i in range(0, 2):
        if i + 1 != carDoor and i + 1 != userChoice:
            hostOptionList[indexCount] = (i + 1)
            indexCount = indexCount + 1
        i = i + 1
    firstChoice = random.choice(hostOptionList)
    userSecondChoice = [1,2,3]
    doorList.remove(firstChoice)
    secondChoice = random.choice(doorList)#0 is to swap, 1 is not to swap
    if secondChoice == 0:
        if userChoice != carDoor:
            swapDoorW = swapDoorW + 1
        else:
            swapDoorL = swapDoorL + 1
    else:
        if userChoice == carDoor:
            noSwapDoorW = noSwapDoorW + 1
        else:
            noSwapDoorL = noSwapDoorL + 1
    totalCounter = totalCounter + 1
    finalTime = time.perf_counter()

print(str(totalCounter) + " total iterations")
print(str(swapDoorW) + " times won after swapping doors")
print(str(swapDoorL) + " times lost after swapping doors")
print(str(noSwapDoorW) + " times won after not swapping doors")
print(str(noSwapDoorL) + " times lost after not swapping doors")

