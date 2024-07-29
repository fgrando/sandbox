#include "mex.h"

void arrayProduct(double x, double *y, double *z, int n);

/* The gateway function */
void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[]) {
    double *inMatrix;       /* 1xN input matrix */
    double *outMatrix;      /* 1xN output matrix */
    double multiplier;      /* input scalar */
    size_t ncols;           /* size of matrix */

    /* Check for proper number of arguments */
    if (nrhs != 2) {
        mexErrMsgIdAndTxt("MyToolbox:arrayProduct:nrhs", "Two inputs required.");
    }
    if (nlhs != 1) {
        mexErrMsgIdAndTxt("MyToolbox:arrayProduct:nlhs", "One output required.");
    }

    /* Make sure the first input argument is scalar */
    if (!mxIsDouble(prhs[0]) || mxIsComplex(prhs[0]) || mxGetNumberOfElements(prhs[0]) != 1) {
        mexErrMsgIdAndTxt("MyToolbox:arrayProduct:notScalar", "Input multiplier must be a scalar.");
    }

    /* Make sure the second input argument is type double */
    if (!mxIsDouble(prhs[1]) || mxIsComplex(prhs[1])) {
        mexErrMsgIdAndTxt("MyToolbox:arrayProduct:notDouble", "Input matrix must be type double.");
    }

    /* Get the value of the scalar input */
    multiplier = mxGetScalar(prhs[0]);

    /* Create a pointer to the real data in the input matrix */
    inMatrix = mxGetPr(prhs[1]);

    /* Get dimensions of the input matrix */
    ncols = mxGetN(prhs[1]);

    /* Create the output matrix */
    plhs[0] = mxCreateDoubleMatrix(1, (mwSize)ncols, mxREAL);

    /* Get a pointer to the real data in the output matrix */
    outMatrix = mxGetPr(plhs[0]);

    /* Call the computational routine */
    arrayProduct(multiplier, inMatrix, outMatrix, (int)ncols);
}
