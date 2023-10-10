import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fft

def biased_autocorr(x): 
    corr = signal.correlate(x, x, mode = 'full', method = 'fft')
    rxx_biased = corr / len(x)
    return rxx_biased

def biased_xcorr(x, y):
    xcorr = signal.correlate(x, y, mode = 'full')
    rxy_biased = xcorr / len(x)
    return rxy_biased

def unbiased_autocorr(x):
    corr = signal.correlate(x, x, mode = 'full')
    rxx_unbiased = np.array([corr[n] / (len(x) - np.abs(len(x) - 1 - n)) for n in range(0, len(corr))])
    return rxx_unbiased


# x: datos de tamaño N
# L: Siendo (L-1) tamaño del lag máximo de autocorrelación i.e. Rxx(l > |L-1|) = 0
# N_FFT: La cantidad de puntos que se usa en la FFT para visualizar el periodograma. 
def periodogram_smoothing(x, L, N_FFT = 500000, window = 'bartlett'):
    N = len(x)
    rxx = biased_autocorr(x) # 2N - 1 de largo
    offset = N - 1 
    rxx = rxx[offset - (L-1) : offset + (L-1) + 1] # autocorr ventaneada o windowed con L
    window = signal.get_window(window = window, Nx=2*L-1, fftbins= False) 
    rxx_windowed = rxx*window

    Rxx = np.abs(fft.fftshift(fft.fft(rxx_windowed, n = N_FFT))) 
    w = fft.fftshift(fft.fftfreq(N_FFT, d=1.0)) * 2 * np.pi

    return Rxx, w
