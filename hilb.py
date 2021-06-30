"""
FIR approximation of Hilbert Transform

MIT license
Copyright (c) 2021 Davi C. M. de Almeida

@author: Davi Carvalho Moreno de Almeida (davicmorenoa@gmail.com)
Tue Jun 29 20:52:55 2021

Versions of the packages used:
    numpy : 1.17.0
    scipy : 1.2.1
"""

import numpy as np
from scipy.signal.windows import get_window

def hilb(L, window='boxcar'):
# Compute the coefficients of length L FIR aproximation of Hilbert Transform
#
# Parameters:
#        L : int 
#            Length of filter (odd number).
#   window : string, float, or tuple 
#            Type of window used (see 'window' parameter of 
#            scipy.signal.windows.get_window for details); retangular window 
#            ('boxcar') is the default window.
# Return:
#        h : numpy.ndarray
#            1D array with filter coefficients
  assert L % 2, "L should be integer and odd"
  window = get_window(window, L, fftbins=False)
  M = L-1
  alpha = M / 2
  n = np.arange(-alpha, 0, 1)
  h =  2/(n*np.pi)*np.sin(n*np.pi/2)**2
  return np.concatenate((h, [0], -h[::-1])) * window