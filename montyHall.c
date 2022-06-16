//import all necessary libraries
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <malloc.h>

//establish int variables
float dataPoints = 0, swapDoor = 0, noSwapDoor = 0, 
userInitialChoice, i = 0, carDoor = 2;
//establish time variable
time_t finalTime;


int main() {
    printf("Monty Hall\n");
    srand(time(0));//randomizes results based on current time
    time_t initialTime = time(NULL);
    while((finalTime - initialTime) < 1) {
        userInitialChoice = (rand() % (3));
        carDoor = (rand() % (3));
        if (carDoor != userInitialChoice){
            swapDoor++;
        } else {
            noSwapDoor++;
        }
        dataPoints++;
        finalTime = time(NULL);
    }
    printf("%d iterations\n", dataPoints);
    printf("%d cars won when door swapped\n", swapDoor);
    printf("%d cars won when door not swapped", noSwapDoor);
}
