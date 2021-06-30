# Description

Simple function that calculates the coefficients of the FIR approximation of Hilbert Transform.

It does the same as the 'hilb' function in Scilab, but in Python.

# Usage
Just pass the filter length and window type as parameters (default is 'boxcar' - rectangular window).

As with the Scilab function, only odd lengths are accepted for the filter (this is in order to take advantage of the various null coefficients and the integer group delay).

# License

MIT License

Copyright (c) 2021 Davi C. M. de Almeida
