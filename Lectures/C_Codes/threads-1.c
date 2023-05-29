#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

pthread_mutex_t mutex;
pthread_cond_t cond;
int turn = 0;

void * ping(void *arg) {
    pthread_mutex_lock(&mutex);
    while (turn != 0) {
        pthread_cond_wait(&cond, &mutex);
    }
    printf("Ping ");
    fflush(stdout);
    turn = 1;
    pthread_cond_signal(&cond);
    pthread_mutex_unlock(&mutex);
    return NULL;
}

void* pong(void* arg) {
    pthread_mutex_lock(&mutex);
    while (turn != 1) {
        printf("waiting...");
        fflush(stdout);
        pthread_cond_wait(&cond, &mutex);
    }
    printf("Pong\n");
    fflush(stdout);
    turn = 0;
    pthread_cond_signal(&cond);
    pthread_mutex_unlock(&mutex);
    return NULL;
}

int main() {
    pthread_t t1, t2;
    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&cond, NULL);

    pthread_create(&t1, NULL, ping, NULL);
    pthread_create(&t2, NULL, pong, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&cond);

    return 0;
}
