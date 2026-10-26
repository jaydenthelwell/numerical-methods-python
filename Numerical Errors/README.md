# Numerical Errors in Python

A small project exploring how computers handle numbers and how numerical errors can affect calculations.

I made this project as a personal exploration of numerical methods covered in my undergraduate physics coursework.

### What I explored

- Floating-point precision and rounding errors
- Overflow and underflow
- Integer overflow using NumPy
- Subtractive cancellation in the quadratic formula
- Approximating sine using a Taylor series

### Tools used

- Python
- NumPy
- Matplotlib

### Running the code

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

Then run:

```bash
python numerical_errors.py
```

The script prints results and displays plots comparing the Taylor series approximation of sine with NumPy's result.