#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char * argv[]) {
	fork();
	fork();
	printf("Hello World!\n");
	return 0; 
}
