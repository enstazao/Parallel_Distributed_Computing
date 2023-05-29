#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
	int id = fork();
	if (id == 0) {
		printf("Hello From Child\n");
	} else {
		printf("Hello From Parent\n");
	}
	return 0;
}
