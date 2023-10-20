import numpy as np
from ahmadsMathLibrary.IterSolver import copy

##EIGENTHINGS

"""
function to get the spectral radius, i.e the largest absolute eigenvalue. 
"""
#function to get the spectral radius, i.e the largest absolute eigenvalue. 
def spectral_radius(A):
  #incorrect logic, its the largest absolute value, so would have to check all of them. any way to get smallest one? negate and power method?
    x0=np.ones(A.shape[0]).astype(float)
    lam, u = get_dominant_eigenpair(A, x0, 1e-10, 1000)
    return lam

"""
alias for the powermethod, returns te largest eigen value and its associated eigenvalue.
"""
#alias for the powermethod, returns the largest eigen value and its associated eigenvalue
def get_dominant_eigenpair(A, x0, tol, maxiter):
    return power_method(A, x0, tol, maxiter)

"""

"""
#gets the second largest eigen value and its associated eigen pair
def get_second_argest_eigenpair(A, x0, tol, maxiter):
    lam1, v1 = get_dominant_eigenpair(A, x0, tol, maxiter)
    B = A - (lam1 / np.dot(v1, v1.T)) * np.outer(v1, v1)
    return power_method(B, x0, tol, maxiter)

#gets all the eigen pairs for a matrix, repeated uses of power method and matrix deflation.
def get_all_eigenpairs(A, x0, tol, maxiter):
    pairs = []
    B = np.copy(A)
    #number of columns of A is the nu,ber of maximum eigen vectors, what happens if not all of them exist?
    for i in range(A.shape[1]):
      [lam, v] = get_dominant_eigenpair(B, x0, tol, maxiter)
      pairs.append((lam, v))
      B = B - (lam / np.dot(v, v.T)) * np.outer(v, v)
    return pairs

#power method to get the largest eigen value and its associated eigen vector
def power_method(A, x0, tol, maxiter):
    n = len(x0)
    x = np.copy(x0)

    for k in range(maxiter):
      u = x/np.linalg.norm(x)
      x = np.dot(A, u)
      lambda1 = np.dot(u, x)
      if np.linalg.norm(np.subtract(x, lambda1*u)) < tol:
        break
    return lambda1, u

#under construction method to get the smallest eigenvalue and its associated eigenvector
def inverse_power_method(A, x0, tol, maxiter): return "Under Construction"


def subspace_iteration(A, W0, maxiter, tol, extract=False):
    """
    This function returns a subspace spanned by the dominant k eigenvectors of A. k is the number of columns of the initial guess W0.

    Args:

    A (List[List[]]): The input matrix.

    W0 ((List[List[]]): Initial Guess.

    maxiter ((List[List[]]): Maximum iterations.

    tol ((List[List[]]): Tolerance to stop at.

    extract (Bool): Wether to extract eigen pairs from the subspace. Will return 2 objects if set to True.

    Returns:

    List[List[]]: A matrix with a similar span as a subspace of the input matrix
    """

    #TODO - implement QR
    k = W0.shape[1]
    V = np.linalg.qr(W0)[0]  # orth(W0) equivalent

    for _ in range(maxiter):
        W = np.dot(A, V)
        V_tild = np.linalg.qr(W)[0]  # orth(W)
        f = np.linalg.norm(np.dot(V.T,V_tild), 'fro')
        dist = np.sqrt(2) * np.sqrt(1 - (f / k))
        V = np.copy(V_tild)
        if dist < tol:
            break
    if not extract:
      return np.round(V,4)

    #TODO - implement diag
    A_tild = np.dot(V.T, np.dot(A, V))
    lambda_vec, U = np.linalg.eig(A_tild)

    Q = np.dot(V, U)
    U = Q

    return lambda_vec, np.round(U, 5)