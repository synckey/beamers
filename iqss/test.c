/* Say hello in C */
#include <stdio.h>
int main() {
    char name[256];
    fgets(name, sizeof(name), stdin);
    printf("Hello %s", name);
    return(0);
}
