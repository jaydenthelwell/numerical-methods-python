# Newton-Raphson Root Finding

A small Python project based on numerical methods from my undergraduate physics coursework.

I explored Newton-Raphson root finding, how the starting guess affects convergence, and how to use a numerical derivative instead of an exact one.

## What I tried

- Finding the roots of `x² - 2` from different starting guesses
- Finding solutions to `tan(x) = x` and plotting the function
- Using central differences to estimate derivatives for Newton-Raphson

Some starting guesses fail or take longer to converge. For `tan(x) = x`, Newton's method can also jump to a root outside the range I was originally looking at.

## Running it

Install NumPy and Matplotlib if needed:

```bash
python3 -m pip install numpy matplotlib
```

From the main repository folder:

```bash
python3 "Root Finding II/newton_raphson.py"
```

The script prints the roots and iteration counts and shows a plot of `tan(x) - x`.
