//import all necessary libraries
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

//establish int variables
size_t swapDoor = 0, noSwapDoor = 0; 
int carDoor = 2, userInitialChoice;
size_t n = 36;

//establish time variable
time_t finalTime;

int main() {
    int *swapDoor = malloc(n);
    swapDoor = malloc(20);
    int *noSwapDoor = malloc(n);
    noSwapDoor = malloc(20);
    printf("Monty Hall\n\nWait 60 seconds...\n\n");
    srand(time(0));//randomizes results based on current time
    time_t initialTime = time(NULL);//takes note of exact time loop started
    while((time(NULL) - initialTime) < 5) {//stops loop at 60 sec
        if (carDoor != (rand() % (3))){
            swapDoor++; //tracks wins when swapping
        } else {
            noSwapDoor++;//tracks wins without swapping
        }
    }
    int *dataPoints = malloc(n);
    dataPoints = malloc(20);
    dataPoints = *swapDoor + *noSwapDoor;
    if (dataPoints < swapDoor){
            printf("had overflow");
    }
    printf("%d datapoints\n", (dataPoints));
    printf("%d cars won when door swapped\n", (swapDoor));
    printf("%d cars won when door not swapped", (noSwapDoor));
    free(dataPoints);
    free(swapDoor);
    free(noSwapDoor);
}
