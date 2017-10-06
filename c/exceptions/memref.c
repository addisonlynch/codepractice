//code for invalid memory reference that triggers a seg fault (abort)
#include <stdio.h>
#include <stdlib.h>

int a[300];

int main(void)
{
a[500] = 3;
return 0;

}