#include <stdio.h>
#include <stdlib.h>

#include <pthread.h>


typedef struct args_t{
  int dim;
  char* name;
}args_t;


void *threadf(void* arg);


int main(void)

{

  pthread_t pid;
  args_t args;
  args.dim = 1;
  args.name = "boomer!";

  if (pthread_create(&pid, NULL, &threadf, (void*)&args) != 0)
    {
      fprintf(stderr, "Thread could not be created!\n");
      exit(-1);
    }

  return pthread_join(pid, NULL);
  


}

void *threadf(void* arg)
{
  args_t *args = arg;
  printf("This is thread %s with dimension %d.", args->name, args->dim);
  return NULL;
  
}
  
