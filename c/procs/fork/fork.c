/*
Inline creation of child process and simple test execution

*/

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <errno.h>
#include <sys/wait.h>

int var_glb;

int main(void)
{
	pid_t child;

	int var_lcl = 0;

	child = fork();

	if(child >= 0) // fork was successful
	{
		if(child == 0) // child process
		{
			var_lcl++;
			var_glb++;
			printf("Child process :: var_lcl = [%d], var_glb = [%d]\n", var_lcl, var_glb);
		}
		else
		{
			var_lcl = 10;
			var_glb = 20;
			printf("Parent process :: var_lcl = [%d], var_glb = [%d]\n", var_lcl, var_glb);
		}
	}
	else
	{
		printf("fork failed. quitting!\n");
return 1;
	}
	return 0;
}