from  ahmadsMathLibrary.linear_algebra import *
from ahmadsMathLibrary.Vector import Vector
from ahmadsMathLibrary.Matrix import Matrix
from ahmadsMathLibrary.IterSolver import IterativeSolverPrivate
import numpy as np
import time

A = [[4, -1, 0, 0],[-1, 4, -1, 0],[0, -1, 4, -1],[0, 0, -1, 3]]
b = [15, 10, 10, 10]
res = IterativeSolverPrivate(A, b, [1.0, 1.0, 1.0, 1.0],10**-10, 10)
print(res.jacobi())
s1=time.time()
test_A = [[1,1, 3, 4],[2,3, 4, 5]] #(2 x 4)
test_A2 = [[1,1],[3,7], [3, 4], [5, 6]] #(4x 2)
test_b = [1,2, 4, 5]
ay = Vector(test_b)
test_matrix = Matrix(test_A)
time
s1=time.time()
res1 = mat_vec_private(test_A,test_b)
s2=time.time()
print(res1, s1, s2, s2-s1)
s3=time.time()
res2 = mat_vec(test_A, test_b)
s4=time.time()
print(res2, s3, s4, s4-s3)
s5=time.time()
res3= mat_mat(test_A, test_A2)
s6=time.time()
print(res3, s5, s6, s6-s5)
s7 = time.time()

res4 = np.dot(test_A, test_A2)
s8 = time.time()
print(res4, s7, 8, s8-s7)
print((s6-s5) - (s8-s7))
#print(ay.add(ay).data)
print(test_matrix.add(test_A).data)
print(ay.self_outer())
print(np.outer(test_b, test_b))
print(ay.self_inner())
print(2.0 + 3)

#[1, 1  * [1, 1 = [1, 1
# 2, 3]    0, 0]   2, 1]