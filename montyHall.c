//import all necessary libraries
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

//establish int variables
int totalCounter = 0, swapDoor = 0, noSwapDoor = 0, secondChoice = 0, userChoice, firstChoice, randIndex, carChoice;
//establish time variable
time_t finalTime;

int main() {
    printf("Monty Hall Sim");
    time_t initialTime = time(NULL);
    while ((finalTime - initialTime) < 5) {
        int doorList[] = {0, 1, 2};
        carChoice = (rand() % (3));
        doorList.Remove(carChoice);
        userChoice = (rand() % (3));
        if (userChoice != carChoice) {
            doorList.Remove(userChoice);
        } 
        firstChoice = doorList[(rand() % (sizeof doorList))];//chooses random index of doors not containing car or chosen by the user
        secondChoice = (rand() % (2));//chooses either 0 or 1, 0 is swap, 1 is no swap
        if (userChoice != carChoice) {
            swapDoor++;
        } else {
            noSwapDoor++;
        }
        totalCounter++;
        finalTime = time(NULL);
}   }
    printf("\n", totalCounter);
    printf("\n", swapDoor);
    printf("\n", noSwapDoor);
    return 0;
