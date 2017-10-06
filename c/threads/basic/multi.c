#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>


typedef struct{

  int dim;
  char* name;
  char* idk;
  int pid;
}thread_args;





void* threadf(void*arg)
{

 thread_args *args = (thread_args*)arg;

  printf("Hello from %s %d!\n", args->name, args->dim);
  return NULL;

}




int main(void)

{
unsigned short MAX_THREADS = 4;
  pthread_t threads[MAX_THREADS];

  thread_args send[MAX_THREADS];


  unsigned short i;
  for(i = 0; i < MAX_THREADS; i++)
    {
      send[i].name = "Thread";
	send[i].idk = "idk";
      send[i].dim=i;
      pthread_create(&threads[i], NULL, threadf, &send[i]);
    }

  for(i = 0; i < MAX_THREADS; i++)
    {
      pthread_join(threads[i], NULL);
    }

  return 0;


}
