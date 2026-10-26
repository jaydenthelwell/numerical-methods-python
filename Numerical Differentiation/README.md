# Numerical Differentiation in Python

A small project exploring how to estimate derivatives numerically, based on methods covered in my undergraduate physics coursework.

### What I explored

- **Forward difference (FD):** Estimates the derivative using two nearby points.
- **Central difference (CD):** Uses points on either side of the value being differentiated.
- **Extrapolated difference (ED):** Combines central difference estimates to improve accuracy.
- **Step size and error:** Compares each method with the exact derivative of `cos(x)`.
- **Subtractive cancellation:** Investigates why very small step sizes can make numerical results less accurate.

### Tools

- Python
- NumPy
- Matplotlib

### Running the code

From the main repository folder, run:

```bash
python3 "Numerical Differentiation/numerical_differentiation.py"
```

The script prints a comparison of errors and displays two plots.

### What I'm learning

A smaller step size does not always give a better approximation. Different methods have different errors, and floating-point rounding becomes important when the step size is very small.
