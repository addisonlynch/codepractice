/*
This program demonstrates a deadlock on the global variable glbcnt



*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>

sem_t mutex[2];
long globcnt = 0;


void* threadf(void* arg) {
    
    int id = (int)arg;
	int i;
    for(i = 0; i < 10; i ++)
    {
    	sem_wait(&mutex[id]); sem_wait(&mutex[1-id]); 
    		globcnt++;
		sem_post(&mutex[id]); sem_wait(&mutex[1-id]);
    }
return NULL;
}

int main(int argc, char** argv) {


    sem_init(&mutex[0], 0, 1);
    sem_init(&mutex[1], 0, 1);
    // initialize semaphore, only to be used with threads in this process, set value to 1
   	const unsigned MAX_THREADS = 2;
   	unsigned i;
    pthread_t *mythread = (pthread_t *)malloc(MAX_THREADS*sizeof(*mythread));;
    // start the threads
    printf("Starting threads...\n");
    pthread_create(&mythread[0], NULL, threadf, (void*)0);
    pthread_create(&mythread[1], NULL, threadf, (void*)1);
    
for(i = 0; i < MAX_THREADS;i++)
{
    pthread_join(mythread[i], NULL);
 }  
    printf("globcnt: %ld\n", globcnt);
    
    return 0;
}
