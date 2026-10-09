# Unruh: False Loss of Coherence (Derivations and Simulations)

Mathematical derivations and numerical simulations based on W. G. Unruh's paper "False loss of coherence" (2000).

## Reference Paper
- Title: False loss of coherence
- Author: William G. Unruh
- Publication: Relativistic Quantum Measurement and Decoherence, ed. F. Petruccione, Springer-Verlag (2000)
- arXiv: arXiv:1110.2199 [quant-ph]
- DOI: 10.48550/arXiv.1110.2199

## Scope and Disclaimer
This repository does not introduce any new physics or theoretical concepts beyond the reference paper. Its scope is limited to:

1. Mathematical derivation: Expanding the intermediate algebraic steps that were condensed or omitted in the original text.
2. Numerical simulation: Implementing the analytical equations to evaluate the system's behavior under numerical computation.

In certain parts of the simulations, variations in parameters and driving profiles are tested. These cases do not represent additional physical concepts, but rather explore configurations that were not the primary focus of the original work.

## Repository Contents

### spin_half_derivations.ipynb
- Contains intermediate mathematical derivations for the spin-1/2 model coupled to a massive scalar field (Section II of the paper).
- Note: The contents of this file were converted from handwritten notes to LaTeX format via an AI assistant. The notation and expressions are currently under manual review.

### spin_half_simulation.ipynb
- Numerical calculation of the field correlation function C(s) and the coherence factor |J(t)|.
- Evaluates adiabatic and non-adiabatic transitions.
- Implements several time-dependent coupling profiles epsilon(t) (such as Gaussian, step, delta-like, and periodic) to examine the conditions for false versus genuine loss of coherence.

## Usage
The notebook parameters (including field mass, interaction profile widths, and temporal grids) can be modified directly to test different regimes.

Dependencies:
- Python >= 3.9
- NumPy
- SciPy
- Matplotlib
- Jupyter
