//import all necessary libraries
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

//establish int variables
int totalCounter = 0, swapDoor = 0, noSwapDoor = 0,
secondChoice = 0, userInitialChoice, firstChoice, randIndex, 
carChoice, i = 0, carDoor = 2;
//establish time variable
time_t finalTime;


int main() {
    srand(time(0));//randomizes results based on current time
    time_t initialTime = time(NULL);
    while((finalTime - initialTime) < 1) {
        userInitialChoice = (rand() % (3));
        carDoor = (rand() % (3));
        
    }
}

int main() {
    printf("Monty Hall Sim");
    time_t initialTime = time(NULL);
    srand(time(0));//randomizes results based on current time
    while ((finalTime - initialTime) < 1) {
        carChoice = (rand() % (3));
        int goatDoors[2];
        int newListIndex = 0;
        for (i = 0; i < 3; i++) {
            if (i != carChoice) {
                goatDoors[newListIndex] = i;
                newListIndex++
            }   
        }
        userChoice = (rand() % (3));
        if userChoice != carChoice {
            int hostOptions [1];
        } else {
            int hostOptions [2];
        }
        newListIndex = 0;
        for (i = 0; i < 2; i++) {
            if (goatDoors[i] != userChoice) {
                hostOptions[newListIndex] = i;
                newListIndex++;
            }
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
        }
    printf("\n%d", totalCounter);
    printf("\n%d", swapDoor);
    printf("\n%d", noSwapDoor);
    return 0;
    }
