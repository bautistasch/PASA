import numpy as np
from scipy import fft
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import butter, freqz, sosfreqz

def get_lowpass(fs, cutoff_frequency, plot_ = False):
    #cutoff_frequency = 1000  # Cutoff frequency in Hz
    filter_order = 8          # Filter order (higher order provides steeper roll-off)
    sampling_frequency = fs  # Sampling frequency in Hz

    nyquist_frequency = 0.5 * sampling_frequency
    normalized_cutoff = cutoff_frequency / nyquist_frequency
    normalized_cutoff_posta = normalized_cutoff / 1.04654
    sos = signal.butter(filter_order, normalized_cutoff_posta, btype='low', analog=False, output='sos')

    # Compute the frequency response
    w, h = signal.sosfreqz(sos, worN=8000)

    # Extract magnitude and phase
    magnitude = 20 * np.log10(abs(h))
    phase = np.angle(h, deg=True)

    if plot_ == True:
        # Plot the Bode plot
        plt.figure(figsize=(9, 5))

        # Magnitude plot
        plt.subplot(2, 1, 1)
        plt.plot(w/(2*np.pi) * sampling_frequency, magnitude, 'b')
        plt.title('Bode Plot - Magnitude Response')
        plt.ylabel('MAgnitude (dB)')
        plt.grid()
        plt.ylim(-80, 2)
        plt.xscale('log')

        plt.tight_layout()
        plt.show()
    return sos
