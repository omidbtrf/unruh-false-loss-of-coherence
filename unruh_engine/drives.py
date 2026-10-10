import numpy as np


def gaussian_drive(t, eps0=1.0, t0=12.0, sigma=2.5):
    val = eps0 * (np.exp(-((t - t0) ** 2) / (2.0 * sigma**2)) - np.exp(-(t0**2) / (2.0 * sigma**2)))
    d_val = -eps0 * ((t - t0) / (sigma**2)) * np.exp(-((t - t0) ** 2) / (2.0 * sigma**2))
    return val, d_val


def periodic_smooth_drive(t, eps0=1.0, omega=2.0, tau_rise=1.0):

    rise = 1.0 - np.exp(-t / tau_rise)
    val = eps0 * rise * np.sin(omega * t)
    
    d_rise = (1.0 / tau_rise) * np.exp(-t / tau_rise)
    d_val = eps0 * (d_rise * np.sin(omega * t) + rise * omega * np.cos(omega * t))
    return val, d_val


def periodic_square_drive(t, eps0=1.0, omega=1.5, sharpness=15.0):

    turn_on = 1.0 - np.exp(-t)
    sin_term = np.sin(omega * t)
    tanh_term = np.tanh(sharpness * sin_term)
    val = eps0 * 0.5 * (1.0 + tanh_term) * turn_on
    
    dt = t[1] - t[0] if len(t) > 1 else 1e-4
    d_val = np.gradient(val, dt)
    return val, d_val


def step_drive(t, eps0=1.0, t_step=2.0, width=0.5):

    sig = 1.0 / (1.0 + np.exp(-(t - t_step) / width))
    sig_0 = 1.0 / (1.0 + np.exp(t_step / width))
    val = eps0 * (sig - sig_0)
    
    d_sig = (1.0 / width) * sig * (1.0 - sig)
    d_val = eps0 * d_sig
    return val, d_val


def delta_drive(t, area=1.0, t_peak=2.5, width=0.08):

    norm = area / (np.sqrt(2.0 * np.pi) * width)
    g = np.exp(-((t - t_peak) ** 2) / (2.0 * width**2))
    g_0 = np.exp(-(t_peak**2) / (2.0 * width**2))
    val = norm * (g - g_0)
    
    d_val = -norm * ((t - t_peak) / (width**2)) * g
    return val, d_val


DRIVE_REGIMES = {
    "gaussian": gaussian_drive,
    "periodic_smooth": periodic_smooth_drive,
    "periodic_square": periodic_square_drive,
    "step": step_drive,
    "delta": delta_drive
}