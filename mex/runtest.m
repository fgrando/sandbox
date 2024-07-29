%setenv('MW_MINGW64_LOC','C:\opt\apps\mingw81')
setenv('MW_MINGW64_LOC','C:\opt\apps\mingw63')
mex code.c glue.c

result = code(2, [1, 2, 3, 4]);
disp(result);  % Output will be [2, 4, 6, 8]

