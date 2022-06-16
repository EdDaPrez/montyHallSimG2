//import all necessary libraries
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

//establish int variables
long long int swapDoor = 0, noSwapDoor = 0; 
int carDoor = 2, userInitialChoice;
//establish time variable
time_t finalTime;

int main() {
    printf("Monty Hall\n\nWait 60 seconds...\n\n");
    srand(time(0));//randomizes results based on current time
    time_t initialTime = time(NULL);//takes note of exact time loop started
    while((time(NULL) - initialTime) < 60) {//stops loop at 60 sec
        userInitialChoice = (rand() % (3));//random int betw 0-2
        if (carDoor != userInitialChoice){
            swapDoor++; //tracks wins when swapping
        } else {
            noSwapDoor++;//tracks wins without swapping
        }
    }
    long long int dataPoints = abs(swapDoor) + abs(noSwapDoor);
    printf("%d datapoints\n", (dataPoints));
    printf("%d cars won when door swapped\n", abs(swapDoor));
    printf("%d cars won when door not swapped", abs(noSwapDoor));
}
