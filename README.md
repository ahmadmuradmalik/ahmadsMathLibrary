# ahmadsMathLibrary

ahmadsMathLibrary is a Python-based numerical methods library designed to offer efficient solutions for complex mathematical challenges. It provides state-of-the-art iterative solvers for solving large-scale linear systems, among other mathematical operations.

## Features

Iterative Solvers: Advanced algorithms that enable precise solutions for linear systems. Currently supports jacobi, Gauss-siedel and Conjugate gradient solver.

Eigen Things: Methods for getting eigenvalues and eigenvectors of matrices. Currently uses the power method for the dominant eigen-pair and then obtaining subsequent pairs using matrix deflation

Linear Algebra: Provides basic functionality for computing common linear algebra operations like Matrix Vector Multiplication, dot products, vector norms. 

Decompositions: Efficient implementation of the Fast Fourier Transform. Can be used to decompose any input signals into corresponding frequencies.


## Installation

To install ahmadsMathLibrary, use pip:

```
pip install ahmadsMathLibrary
```


## Usage

Here's a simple example of using the library:
```python
from ahmadsMathLibrary.IterSolver import IterativeSolver

A, b = [[1, 2], [3, 4]], [5, 6]

x0, tol, maxiter = [0, 0], 1**-10, 25

mySolver = IterativeSolver(A,b,x0,tol,maxiter)

mySolver.conjugategradient()
```
### or 

```python 
from ahmadsMathLibrary import eigenthings

A = [[1,0],
     [0,1]]

largest_eigenvalue = eigenthings.spectral_radius(A)
```
## Documentation
Detailed documentation can be found in my head

## Contribution
Contributions are always welcome! Please read the contribution guidelines if you can find them.

## License

MIT License, see license.txt for more



