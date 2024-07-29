#if CODE
#include "stdio.h"
#define PRINT printf
#else
#include "mex.h"
#define PRINT mexPrintf
#endif

#define MATRIX_cell(M, row, col, i,j) M[(i*col+j)]

void mod_matrix(double *m1, int m1_m, int m1_n, 
                double *m2, int m2_m, int m2_n,
                double *o1)
{
    PRINT("m=%d n=%d\n", m1_m, m1_n);

    int i, j;
    for (i = 0; i < m1_m; i++) {
        for (j = 0; j < m1_n; j++) {    
            PRINT("%d,%d = %f\n", i, j, MATRIX_cell(m1, m1_m, m1_n, i, j));
        }
    }
    
    PRINT("m=%d n=%d\n", m2_m, m2_n);
    
    for (i = 0; i < m2_m; i++) {
        for (j = 0; j < m2_n; j++) {    
            PRINT("%d,%d = %f\n", i, j, MATRIX_cell(m2, m2_m, m2_n, i, j));
        }
    }
   
    for (i = 0; i < m1_m; i++) {
        for (j = 0; j < m1_n; j++) {    
            MATRIX_cell(o1, m1_m, m1_n, i, j) = MATRIX_cell(m1, m1_m, m1_n, i, j)*2 ;
        }
    }
}
