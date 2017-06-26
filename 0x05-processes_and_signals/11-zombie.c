#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/wait.h>

/**
 * infite_while - starts an infiinte loop, pausing for 1 second each round
 * Return: void
 */
int infite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - entry point for the zombie program
 * Return: void
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
			exit(0);
		printf("Zombie process created, PID: %u\n", pid);
	}
	infite_while();
	return (0);
}
