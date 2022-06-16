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
    time_t initialTime = time(NULL);//takes note of exact time loop started
    while((finalTime - initialTime) < 1) {//stops loop at 60 sec
        userInitialChoice = (rand() % (3));//random int betw 1-3
        carDoor = (rand() % (3));//random int betw 1-3
        if (carDoor != userInitialChoice){
            swapDoor++; //tracks wins when swapping
        } else {
            noSwapDoor++;//tracks wins without swapping
        }
        dataPoints++;//tracks total iterations
        finalTime = time(NULL);
    }
    printf("%d iterations\n", dataPoints);
    printf("%d cars won when door swapped\n", swapDoor);
    printf("%d cars won when door not swapped", noSwapDoor);
}
