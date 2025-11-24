# Implement this for the system H(z)=(0.5(z-0.7)(z-0.9))/(z-0.6)(z-0.4)  and verify whether the system is stable or unstable

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

num = [0.5, -0.8, 0.315]
den = [1, -1.0, 0.24]

zeros = np.roots(num)
poles = np.roots(den)

print("Zeros:", zeros)
print("Poles:", poles)

stable = np.all(np.abs(poles) < 1)
print("Stability:", "Stable" if stable else "Unstable")

plt.figure(figsize=(6, 6))
theta = np.linspace(0, 2*np.pi, 400)
plt.plot(np.cos(theta), np.sin(theta), 'k--')

plt.scatter(zeros.real, zeros.imag, s=80, facecolors='none', edgecolors='b')
plt.scatter(poles.real, poles.imag, s=80, marker='x', color='r')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title("Pole-Zero Plot")
plt.xlabel("Real(z)")
plt.ylabel("Imag(z)")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()
plt.show()

w, H = freqz(num, den, worN=1024)
mag_db = 20 * np.log10(np.abs(H) + 1e-12)
phase_deg = np.unwrap(np.angle(H)) * 180 / np.pi

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(w, mag_db)
plt.title("Frequency Response")
plt.ylabel("Magnitude (dB)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(w, phase_deg)
plt.xlabel("Frequency (rad/sample)")
plt.ylabel("Phase (degrees)")
plt.grid(True)

plt.tight_layout()
plt.show()
