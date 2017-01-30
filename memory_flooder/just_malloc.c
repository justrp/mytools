#include <stdlib.h>
#include <unistd.h>

int main()
{
        int size = 4000000;
        char * str = (char *) malloc(size);
        printf("memory allocated\n");
        sleep(10000);
        return 0;
}
