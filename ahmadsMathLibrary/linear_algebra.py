import math
from .Matrix import Matrix
from .Vector import Vector 

def mat_vec_private(matrix, vector):

    """Multiply a matrix with a vector."""
    my_matrix = Matrix(matrix)
    my_vector = Vector(vector)
    if my_matrix.cols != my_vector.size:
        raise ValueError("Matrix column size should match vector size.")
    
    result = []
    for row in my_matrix.data:
        res = 0
        for j, value in enumerate(row):
            res += value * my_vector.data[j]
        result.append(res)
    result = Vector(result)
    return result.data

def mat_mat(matrix1, matrix2):

    matrix1 = Matrix(matrix1) if not isinstance(matrix1, Matrix) else matrix1
    matrix2 = Matrix(matrix2) if not isinstance(matrix2, Matrix) else matrix2

    if matrix1.cols != matrix2.rows:
        return ValueError("Dimension mismatch!", (matrix1.size), (matrix2.size))
    n, m = matrix1.size
    k = matrix2.size[1]
    """
    1) standard method of iterating through all k matvecs 
    2) a (n x m) x (m x k) = k m length matvecs, stacked vertically 
    """
    result = []
    data=matrix2.data
    #number of matvecs
    for i in range(k):
        #do ith matvec
        ith_vec = []
        for j in range(m):
            ith_vec.append(data[j][i])
        result.append(mat_vec_private(matrix1.data, ith_vec))

    return result

def mat_vec(matrix, vector):

    """Multiply a matrix with a vector."""

    if len(matrix[0]) != len(vector):
        raise ValueError("Matrix column size should match vector size.")
    
    result = []
    for row in matrix:
        res = 0
        for j, value in enumerate(row):
            res += value * vector[j]
        result.append(res)
    
    return result


def dot(u, v):
  return sum(ui * vi for ui, vi in zip(u, v))

def norm(x, y=0, type='2'):
    #vector norms

    if type not in ['1', '2', 'inf']:
        return ValueError("invalid norm type, options are '1', '2', 'inf'. defaults to '2'")
    if y==0:
        y= [0] * len(x)
    if len(x) != len(y):
        return ValueError("Vector dimensions do not match")
    diff = [xi-yi for xi,yi in zip(x,y)]
    if type=='1':
        return sum([abs(si) for si in diff])
    if type=='2':
        #print("invlaid norm type, giving the default 2 norm")
        return math.sqrt(sum([si**2 for si in diff]))
    if type =='inf':
        return max([abs(si) for si in diff])
    

    

