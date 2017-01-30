#include <stdlib.h>
#include <unistd.h>

int main()
{
        int size = 4000000;
        char * str = (char *) malloc(size);
        for (int i = 0; i < size; i ++)
            str[i] = (size-i) % sizeof(char); 
        printf("memory filled\n");
        sleep(10000);
        return 0;
}
