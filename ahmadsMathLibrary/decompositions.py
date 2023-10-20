import numpy as np

def fft(y):
    """
    Compute the one-dimensional discrete Fourier Transform.

    This function computes the one-dimensional *n*-point discrete Fourier
    Transform (DFT) with the efficient Fast Fourier Transform (FFT)
    algorithm [CT].

    Parameters
    ----------
    y : array_like
        Input array, can be complex.

    Returns
    -------
    y_hat : complex array
        

    Raises
    ------
    ValueError
        If length of y is not a power of 2

    Notes
    -----
    FFT (Fast Fourier Transform) refers to a way the discrete Fourier
    Transform (DFT) can be calculated efficiently, by using symmetries in the
    calculated terms.  The symmetry is highest when `n` is a power of 2, and
    the transform is therefore most efficient for these sizes.

    References
    ----------
    .. [CT] Cooley, James W., and John W. Tukey, 1965, "An algorithm for the
            machine calculation of complex Fourier series," *Math. Comput.*
            19: 297-301.
    """
      
    N = len(y)
    if N == 1:
        y_hat = y
        return y_hat
    elif N&(N-1):
        raise ValueError('N is not a power of 2')
    else:
        evens = y[::2]
        odds = y[1::2]
        DFT = np.zeros(N//2, dtype=complex)
        for k in range(N//2):
            DFT[k] = np.exp(-2*np.pi*1j*(k)/N)
        u = fft(evens)
        v = DFT * fft(odds)
        y_hat = np.concatenate((u+v, u-v))
        return y_hat

def pca(A, k):
    #returns the first k principal components?
    return 1