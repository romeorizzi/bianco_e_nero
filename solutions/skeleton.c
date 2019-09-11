#include <stdio.h>
#include <stdlib.h>

static const int YES = 1;

static const int NO = 0;


int collana(int n, int *c, void taglia_e_cuci(int a, int b));


int main() {
    // checkpoint
    printf("%d\n", 0);
    // read n
    static int n;
    fflush(stdout);
    scanf("%d", &n);
    // for i to n {...}
    static int *c;
    c = malloc(n * sizeof(*c));
    for (int i = 0; i < n; i++) {
        // read c[i]
        fflush(stdout);
        scanf("%d", &c[i]);
    }
    // call min_mosse = collana(n, c) callbacks {...}
    static int min_mosse;
    {
        void taglia_e_cuci(int a, int b) {
            // callback taglia_e_cuci
            printf("%d %d\n", 1, 0);
            // write a, b
            printf("%d %d\n", a, b);
        }
        min_mosse = collana(n, c, taglia_e_cuci);
    }
    // no more callbacks
    printf("%d %d\n", 0, 0);
    // write min_mosse
    printf("%d\n", min_mosse);
    // exit
    exit(0);
}
