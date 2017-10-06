#include <stdio.h>
#include <stdlib.h>

int main (void)
{
  int x = 0, y = 0;
  printf("x: %d, y: %d\n", x, y);
  while(++x < 10000);
  while(++y < 10000);
  printf("x: %d, y: %d\n", x, y);
  return 0;
}
