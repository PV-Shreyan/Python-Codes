# Write a Python function to compute the Z-transform of an unit step function. verify whether the system is stable or unstable

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

def z_transform_unit_step(truncate=None):
    Z_expr = "1 / (1 - z**(-1))"
    ROC = "|z| > 1 (causal; ROC outside the outermost pole at z=1)"

    finite_expr = None
    if truncate is not None and int(truncate) >= 0:
        N = int(truncate)
        finite_expr = f"(1 - z**({-(N+1)})) / (1 - z**(-1))   (finite-sum N={N})"

    return Z_expr, ROC, finite_expr

def check_stability_from_roc(roc_description):
    includes_unit_circle = "1" in roc_description and ">" in roc_description and roc_description.strip().startswith("|z| > 1") == False

    if ">|z|" in roc_description or "|z| > 1" in roc_description:
        return False
    if "|z| < 1" in roc_description:
        return True
    return False

def pole_zero_plot_unit_step():
    """
    Plot pole (=1) and the unit circle to visualise ROC relative to unit circle.
    """
    fig, ax = plt.subplots(figsize=(5,5))
    theta = np.linspace(0, 2*np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), '--', lw=0.8, label='unit circle')
    ax.scatter([1.0], [0.0], marker='x', color='red', s=80, label='pole at z=1')
    ax.set_aspect('equal', 'box')
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')
    ax.set_title('Pole-zero / ROC illustration for u[n]')
    ax.grid(True, linestyle=':')
    ax.legend()
    plt.tight_layout()
    return fig, ax

def demo_truncated_response_and_freq(truncate=128):
    N = int(truncate)
    h = np.ones(N+1)

    w, H = freqz(h, [1], worN=1024)
    mag_db = 20 * np.log10(np.abs(H) + 1e-12)
    phase_deg = np.unwrap(np.angle(H)) * 180/np.pi

    fig, axs = plt.subplots(2,1, figsize=(9,5), sharex=True)
    axs[0].plot(w, mag_db)
    axs[0].set_ylabel('Magnitude (dB)')
    axs[0].set_title(f'Freq resp of truncated u[n] (Length={N+1})')
    axs[0].grid(True, linestyle=':')

    axs[1].plot(w, phase_deg)
    axs[1].set_ylabel('Phase (deg)')
    axs[1].set_xlabel('Frequency (rad/sample)')
    axs[1].grid(True, linestyle=':')
    plt.tight_layout()
    return fig, axs

if __name__ == "__main__":
    Z_expr, ROC, finite_expr = z_transform_unit_step(truncate=20)
    print("Unilateral Z-transform of the causal unit-step u[n]:")
    print("  X(z) =", Z_expr)
    print("  Typical ROC:", ROC)
    if finite_expr is not None:
        print("  Finite-sum (N=20) closed-form:", finite_expr)
    print()

    stable = check_stability_from_roc(ROC)
    print("Stability check (BIBO):", "Stable (unit circle inside ROC)" if stable else "Unstable (unit circle NOT included in ROC)")
    print()

    pole_zero_plot_unit_step()
    plt.show()

    demo_truncated_response_and_freq(truncate=256)
    plt.show()
