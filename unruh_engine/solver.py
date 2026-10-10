import numpy as np
from scipy.integrate import trapezoid


def compute_decoherence(t_grid, C_real, eps_values, d_eps_values=None):

    dt = t_grid[1] - t_grid[0]
    num_pts = len(t_grid)

    if d_eps_values is None:
        d_eps_values = np.gradient(eps_values, dt)

    C_0 = C_real[0]

    I_1 = (eps_values ** 2) * C_0

    I_2 = np.zeros(num_pts)
    inner_int_past = np.zeros(num_pts)

    for n in range(1, num_pts):
        d_eps_past = d_eps_values[:n + 1]
        C_past = C_real[:n + 1][::-1]
        inner_val = trapezoid(d_eps_past * C_past, dx=dt)
        inner_int_past[n] = inner_val
        I_2[n] = 2.0 * eps_values[n] * inner_val


    integrand_I3 = d_eps_values * inner_int_past
    I_3 = np.zeros(num_pts)
    for n in range(1, num_pts):
        I_3[n] = trapezoid(integrand_I3[:n + 1], dx=dt)

    Gamma = I_1 + I_2 + I_3
    J_abs = np.exp(-2.0 * Gamma)

    return {
        "I_1": I_1,
        "I_2": I_2,
        "I_3": I_3,
        "Gamma": Gamma,
        "J_abs": J_abs
    }