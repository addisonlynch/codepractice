#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

void *inc_x(void *x_void_ptr)
{
  int *x_ptr = (int *)x_void_ptr;
  while(++(*x_ptr) < 10000);
  printf("x increment finished.\n");
  return NULL;
}

int main(void)
{

  int x = 0, y= 0;
  printf("x: %d, y: %d\n", x, y);

  pthread_t xthread;

  if(pthread_create(&xthread, NULL, inc_x, &x))
    {
      fprintf(stderr, "Error creating thread!\n");
      return 1;}

  while(++y < 10000);
  printf("y increment finished.\n");

  if(pthread_join(xthread, NULL))
    {
      fprintf(stderr, "Error joining thread!\n");
      return 2;
    }

  printf("x: %d, y: %d\n", x, y);
  return 0;
  



}
