/*

Data race on globcnt

*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>

sem_t semaphore;
volatile long globcnt = 0;
void* threadf(void* arg) {
    int cnt = 0;
    long i;
    long niters = *((long*)arg);
    for(i = 0; i < niters; i ++)
    {
    	globcnt++;
    }
return NULL;
}

int main(int argc, char** argv) {
    long niters;
    niters = atoi(argv[1]);
    // initialize semaphore, only to be used with threads in this process, set value to 1
   const unsigned MAX_THREADS = 2;
    pthread_t *mythread = (pthread_t *)malloc(MAX_THREADS*sizeof(*mythread));;

    // start the threads
    printf("Starting threads...\n");
    unsigned i;
    for(i = 0; i < MAX_THREADS; i++)
    {
    pthread_create(&mythread[i], NULL, threadf, &niters);
}
for(i = 0; i < MAX_THREADS;i++)
{
    pthread_join(mythread[i], NULL);
 }  
    printf("globcnt: %ld\n", globcnt);
    
    return 0;
}
