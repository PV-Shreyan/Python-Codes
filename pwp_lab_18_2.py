# Use Python to implement both cross-correlation and autocorrelation on a set of audio files (clean_audio.wav, noisy_audio.wav, periodic_audio.wav). Visualize and compare the results.

import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import correlate

files = [r'C:\Users\PV shreyan\Videos\bleep-41488.mp3',
         r'C:\Users\PV shreyan\Videos\bleep-126625.mp3',
         r'C:\Users\PV shreyan\Videos\bleep-censorship-sound-wav-74691.mp3']


audios = [sf.read(f)[0] for f in files]

for i in range(len(audios)):
    if audios[i].ndim > 1:
        audios[i] = audios[i][:, 0]

autocorr = [correlate(a, a, mode='full') for a in audios]

cross_corr_clean_noisy = correlate(audios[0], audios[1], mode='full')
cross_corr_clean_periodic = correlate(audios[0], audios[2], mode='full')

plt.figure(figsize=(12, 8))

for i, ac in enumerate(autocorr):
    plt.subplot(4, 1, i + 1)
    plt.plot(ac)
    plt.title(f'Autocorrelation: {files[i]}')

plt.subplot(4, 1, 4)
plt.plot(cross_corr_clean_noisy, label='Clean vs Noisy')
plt.plot(cross_corr_clean_periodic, label='Clean vs Periodic')
plt.title('Cross-Correlation')
plt.legend()

plt.tight_layout()
plt.show()
