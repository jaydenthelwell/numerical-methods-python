# Numerical Methods in Python

A collection of small Python projects exploring numerical methods and computational techniques used in physics.

I'm an undergraduate Physics student at Queen Mary University of London, and I've been using Python to develop my understanding of numerical methods alongside my degree.

These projects are based on topics introduced in my university coursework, which I've adapted into small experiments to practise coding and explore how different numerical methods work.

## Projects

### 1. Numerical Errors
Exploring the limitations of computer arithmetic, including floating-point precision, overflow and underflow, subtractive cancellation, and approximating sine using a Taylor series.

### 2. Root Finding I
Implementing the bisection and regula falsi methods to find roots of functions and comparing their convergence.

### 3. Numerical Differentiation
Using forward, central and extrapolated differences to approximate derivatives. Investigating how step size affects accuracy and how rounding errors become more significant for very small steps.

### 4. Root Finding II
Exploring the Newton-Raphson method, including how starting guesses affect convergence and how numerical differentiation can be used to estimate derivatives.

## Tools

- Python
- NumPy
- Matplotlib

## Running the projects

Each project has its own folder containing a Python script and a short README explaining what it explores.

To run a script, install NumPy and Matplotlib:

```bash
python3 -m pip install numpy matplotlib
```

Then run the relevant Python file from the repository's main directory. For example:

```bash
python3 "Root Finding II/newton_raphson.py"
```

## About

I'm using this repository to practise scientific programming and build a better understanding of computational methods in physics. I'll continue adding projects as I learn more.