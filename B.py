# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:10:23 2023

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

print("Nama: Arif Wardana")
print("NRP: 5009211030")

# Membuat sinyal contoh
fs = 1000  # Frekuensi sampel (Hz)
t = np.arange(0, 1, 1/fs)  # Waktu dari 0 hingga 1 detik dengan interval sampel
f1 = 5  # Frekuensi komponen 1 (Hz)
f2 = 20  # Frekuensi komponen 2 (Hz)
signal = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Melakukan FFT pada sinyal
fft_result = fft(signal)
fft_freqs = np.fft.fftfreq(len(signal), 1/fs)  # Menghitung frekuensi

# Plot hasil FFT
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Sinyal Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Amplitudo')

plt.subplot(2, 1, 2)
plt.plot(fft_freqs, np.abs(fft_result))
plt.title('Hasil FFT')
plt.xlabel('Frekuensi (Hz)')
plt.ylabel('Amplitudo')

plt.tight_layout()
plt.show()

