#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>


void *
child(void *arg) {
    printf("child\n");
    // signal here: child is done
    return NULL;
}

int
main(int argc, char *argv[]) {
    printf("parent: begin\n");
    pthread_t c;
    c = (pthraed_t*)malloc(sizeof(*c));
    pthread_create(c, NULL, child, NULL);
    // wait here for child

    printf("parent: end\n");
    return 0;
}