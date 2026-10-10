import numpy as np
from scipy.integrate import quad, trapezoid


def gaussian_profile(x, sigma_x=1.0):

    return np.exp(-x**2 / (2.0 * sigma_x**2)) / (np.sqrt(2.0 * np.pi) * sigma_x)


def compute_htilde_sq(h_func, k_grid, x_min=-8.0, x_max=8.0, limit=200):

    def ft_single_k(k_val):
        r, _ = quad(lambda x: np.real(h_func(x) * np.exp(-1j * k_val * x)), x_min, x_max, limit=limit)
        i, _ = quad(lambda x: np.imag(h_func(x) * np.exp(-1j * k_val * x)), x_min, x_max, limit=limit)
        return r**2 + i**2

    return np.array([ft_single_k(k) for k in k_grid])


def compute_correlation_C(s_values, h_func=None, m=1.0, sigma_x=1.0, 
                          x_min=None, x_max=None, k_max=None, n_k=1000):

    if h_func is None:
        h_func = lambda x: gaussian_profile(x, sigma_x=sigma_x)

    if x_min is None:
        x_min = -8.0 * sigma_x
    if x_max is None:
        x_max = 8.0 * sigma_x
    if k_max is None:
        k_max = 10.0 / sigma_x

    k_grid = np.linspace(0.0, k_max, n_k)
    omega = np.sqrt(k_grid**2 + m**2)

    h_t = compute_htilde_sq(h_func, k_grid, x_min=x_min, x_max=x_max)
    W = h_t / (2.0 * np.pi * omega)

    C_val = []
    for s in s_values:
        core = W * np.exp(-1j * omega * s)
        val = 2.0 * trapezoid(core, k_grid)
        C_val.append(val)

    return np.array(C_val)