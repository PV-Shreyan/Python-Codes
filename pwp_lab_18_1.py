# Use Python to create a script that performs both linear and circular convolution on an audio file with an impulse response. Compare and visualize the results.

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import convolve

audio, sr = sf.read('C:/Users/PV Shreyan/Downloads/Fly Away.wav')
impulse, _ = sf.read('C:/Users/PV Shreyan/Downloads/Fly Away.wav')

if audio.ndim > 1:
    audio = audio[:, 0]
if impulse.ndim > 1:
    impulse = impulse[:, 0]

linear_conv = convolve(audio, impulse, mode='full')

N = len(audio)
M = len(impulse)
circular_len = N
impulse_padded = np.pad(impulse, (0, N-M), 'constant')
circular_conv = np.fft.ifft(np.fft.fft(audio) * np.fft.fft(impulse_padded)).real

sf.write('linear_conv.wav', linear_conv, sr)
sf.write('circular_conv.wav', circular_conv, sr)

plt.figure(figsize=(12,6))
plt.subplot(3,1,1)
plt.plot(audio)
plt.title('Original Audio')
plt.subplot(3,1,2)
plt.plot(linear_conv)
plt.title('Linear Convolution')
plt.subplot(3,1,3)
plt.plot(circular_conv)
plt.title('Circular Convolution')
plt.tight_layout()
plt.show()
