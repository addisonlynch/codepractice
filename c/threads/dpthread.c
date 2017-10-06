#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>

sem_t semaphore;
int globcnt = 0;
void* threadf() {
    int cnt = 0;
    unsigned i;
    for(i = 0; i < 1000; i ++)
    {
    	cnt++;
    }
globcnt += cnt;
return NULL;
 

}

int main(void) {
    
    // initialize semaphore, only to be used with threads in this process, set value to 1
   
    pthread_t *mythread;
    
    mythread = (pthread_t *)malloc(sizeof(*mythread));
    
    // start the thread
    printf("Starting thread, semaphore is unlocked.\n");
    pthread_create(mythread, NULL, threadf, NULL);
    pthread_join(*mythread, NULL);
   
    printf("globcnt: %d\n", globcnt);
    
    return 0;
}