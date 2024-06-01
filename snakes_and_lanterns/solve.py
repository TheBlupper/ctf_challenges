from sage.all import *
n = 8
N = 97
R = Zmod(N)

base =  vector(R, (38, 51, 7, 6, 5, 37, 13, 65, 89, 69, 64, 18, 33, 0, 38, 52, 24, 54, 78, 53, 55, 40, 55, 96, 8, 39, 95, 1, 56, 28, 21, 1, 9, 91, 53, 11, 13, 42, 29, 61, 86, 61, 92, 40, 48, 52, 87, 68, 93, 35, 58, 94, 5, 12, 48, 90, 9, 14, 26, 35, 89, 85, 1, 67))

A = zero_matrix(R, n*n, n*n)
for i in range(n):
    for j in range(n):
        A[n*i+j, n*i+j] = 1
        if i > 0:
            A[n*i+j, n*(i-1)+j] = 1
        if i < n-1:
            A[n*i+j, n*(i+1)+j] = 1
        if j > 0:
            A[n*i+j, n*i+j-1] = 1
        if j < n-1:
            A[n*i+j, n*i+j+1] = 1
print(bytes(ZZ(x)+32 for x in A**-1*-base).decode())