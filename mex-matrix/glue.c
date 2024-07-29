#include "mex.h"

void mod_matrix(double *m1, int m1_m, int m1_n, 
                double *m2, int m2_m, int m2_n,
                double *o1);

/* The gateway function */
void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[]) {
    double *mat1, *mat2;    /* 1xN input matrix */
    double *outMatrix;      /* 1xN output matrix */


    /* Check for proper number of arguments */
    if (nrhs != 2) {
        mexErrMsgIdAndTxt("mod_matrix:nrhs", "Two inputs required.");
    }
    if (nlhs != 1) {
        mexErrMsgIdAndTxt("mod_matrix:nlhs", "One output required.");
    }

    /* Make sure the second input argument is type double */
    if (!mxIsDouble(prhs[0]) || mxIsComplex(prhs[0])) {
        mexErrMsgIdAndTxt("mod_matrix:notDouble", "Input matrix must be type double.");
    }
    
    /* Make sure the second input argument is type double */
    if (!mxIsDouble(prhs[1]) || mxIsComplex(prhs[1])) {
        mexErrMsgIdAndTxt("mod_matrix:notDouble", "Input matrix must be type double.");
    }

    /* Get the value of the scalar input */
    mat1 = mxGetPr(prhs[0]);
    size_t mat1_n = mxGetN(prhs[0]);
    size_t mat1_m = mxGetM(prhs[0]);
    
    /* Create the output matrix */
    plhs[0] = mxCreateDoubleMatrix((mwSize)mat1_m, (mwSize)mat1_n, mxREAL);

    /* Get a pointer to the real data in the output matrix */
    outMatrix = mxGetPr(plhs[0]);

    mat2 = mxGetPr(prhs[1]);
    size_t mat2_n = mxGetN(prhs[1]);
    size_t mat2_m = mxGetM(prhs[1]);

    
    /* Call the computational routine */
    mod_matrix(mat1, mat1_m, mat1_n, mat2, mat2_m, mat2_n, outMatrix);
}
