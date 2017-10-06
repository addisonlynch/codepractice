/*
Forks child process, runs separate function for parent and child

*/
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>

void childProc(int arg)
{
	int val = arg;
	int pid = getpid();
	printf("This is child process %d passed val %d.\n", pid, val);
	return;
}


void parentProc(int arg)
{
	int val = arg;
	int pid = getpid();
	printf("This is parent process %d passed val %d.\n", pid, val);
	return;
}

int main(void)
{
pid_t pid = fork();
int val = 5;
if(pid ==0)
{
	childProc(val);
}	
else
	parentProc(val);

return 0;
}