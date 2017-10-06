/* A simple producer consumer problem - REPAIRED(in progress)!

$ ./pc 5
prints 0 1 2 3 4

$ ./pc 100000
causes some problems!

*/


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>

sem_t mutex;
int max = 1000;
int buf[1000];
int fill = 0;
int loops = 0; 
int use=0;



typedef struct{
	int *buf;
	int n;
	int front;
	int rear;
	sem_t mutex;
	sem_t slots;
	sem_t items;
}sbuf_t;

void sbuf_init(sbuf_t* sp, int n);

void sbuf_init(sbuf_t* sp, int n){
	sp->buf = calloc(n, sizeof(int));
	sp->n = n;
	sp->front = sp->rear = 0;
	sem_init(&sp->mutex, 0, 1);
	sem_init(&sp->slots, 0, n);
	sem_init(&sp->items, 0, 0);
}

void sbuf_deinit(sbuf_t* sp);

void sbuf_deinit(sbuf_t* sp){
	free(sp->buf);
}
void sbuf_insert(sbuf_t* sp, int item){
	sem_wait(&sp->slots);
	sem_wait(&sp->mutex);
	sp->buf[(++sp->rear)%(sp->n)] = item;
	sem_post(&sp->mutex);
	sem_post(&sp->item);
}
int sbuf_remove(sbuf_t* sp);

int sbuf_remove(sbuf_t* sp)
{
	int item;
	sem_wait(&sp->items);
	sem_wait(&sp->mutex);
	item = sp->buf[(++sp->front)%(sp->n)];
	sem_post(&sp->mutex);
	sem_post(&sp->slots);
	return item.
}


void put(int value){
	buf[fill] = value;
	fill = (fill+1) % max;
}

int get(){
	int tmp = buf[use];
	use = (use +1) % max;
	return tmp;
}

void* producer(void* arg) {
    long i;;
    for(i = 0; i < loops; i ++)
    {
    	int tmp = get();
    	printf("%d\n", tmp);
    }
return NULL;
}

void* consumer(void* arg) {
    long i;
    for(i = 0; i < loops; i ++)
    {
    	put(i);
    }
return NULL;
}

int main(int argc, char** argv) {
    loops = atoi(argv[1]);
    // initialize semaphore, only to be used with threads in this process, set value to 1
    const unsigned MAX_THREADS = 2;
    pthread_t *mythread = (pthread_t *)malloc(MAX_THREADS*sizeof(*mythread));;

    // start the threads
    printf("Starting threads...\n");
    unsigned i;
    pthread_create(&mythread[0], NULL, producer, NULL); 
    pthread_create(&mythread[1], NULL, consumer, NULL); 

for(i = 0; i < MAX_THREADS;i++)
{
    pthread_join(mythread[i], NULL);
 }  
    return 0;
}
