import numpy as np
import matplotlib.pyplot as plt


# Newton-Raphson using an exact derivative

def newton_step(f, fp, x):
    derivative = fp(x)
    if abs(derivative) < 1e-14:
        raise ValueError("Derivative is too close to zero")
    return x - f(x) / derivative


def newton_root(f, fp, x0, tolerance=1e-8, max_iterations=35):
    x = float(x0)
    if abs(f(x)) < tolerance:
        return x, 0

    for n in range(1, max_iterations + 1):
        new_x = newton_step(f, fp, x)
        if not np.isfinite(new_x):
            raise ValueError("Iteration produced a non-finite value")
        if abs(new_x - x) < tolerance and abs(f(new_x)) < tolerance:
            return new_x, n
        x = new_x
    raise ValueError("Did not converge within the iteration limit")


# Find the roots of x^2 - 2

def f(x):
    return x**2 - 2


def fp(x):
    return 2*x


print("Newton-Raphson for x^2 - 2")
for guess in [1, -1, 1e5, 0, 1e-8]:
    try:
        root, steps = newton_root(f, fp, guess)
        print(f"Start {guess:g}: root = {root:.10f}, iterations = {steps}, f(root) = {f(root):.2e}")
    except ValueError as error:
        print(f"Start {guess:g}: {error}")


# A trickier example: tan(x) = x

def g(x):
    return np.tan(x) - x


def gp(x):
    return np.tan(x)**2  # sec(x)^2 - 1


print("\nNewton-Raphson for tan(x) = x")
for guess in [0, 0.1, 4, 4.5, 7.7, 8]:
    try:
        root, steps = newton_root(g, gp, guess)
        print(f"Start {guess:g}: root = {root:.10f}, iterations = {steps}, g(root) = {g(root):.2e}")
    except ValueError as error:
        print(f"Start {guess:g}: {error}")

# Plot tan(x) - x, hiding the jumps near tan(x)'s asymptotes
x = np.linspace(0, 10, 4000)
y = g(x)
y[np.abs(np.cos(x)) < 0.03] = np.nan
plt.plot(x, y, linewidth=1)
plt.axhline(0, color="black", linewidth=0.8)
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("tan(x) - x")
plt.title("Roots of tan(x) = x")
plt.grid(True)
plt.tight_layout()
plt.show()


# Newton-Raphson using a numerical derivative (central difference)

def CD(f, x, h=1e-5):
    return (f(x + h/2) - f(x - h/2)) / h


def newton_CD_step(f, x):
    derivative = CD(f, x)
    if abs(derivative) < 1e-14:
        raise ValueError("Numerical derivative is too close to zero")
    return x - f(x) / derivative


def newton_CD_root(f, x0, tolerance=1e-8, max_iterations=35):
    x = float(x0)
    if abs(f(x)) < tolerance:
        return x, 0

    for n in range(1, max_iterations + 1):
        new_x = newton_CD_step(f, x)
        if not np.isfinite(new_x):
            raise ValueError("Iteration produced a non-finite value")
        if abs(new_x - x) < tolerance and abs(f(new_x)) < tolerance:
            return new_x, n
        x = new_x
    raise ValueError("Did not converge within the iteration limit")


print("\nUsing central differences instead of an exact derivative")
for name, function, guess in [("x^2 - 2", f, 1), ("tan(x) - x", g, 4.5), ("tan(x) - x", g, 7.7)]:
    try:
        root, steps = newton_CD_root(function, guess)
        print(f"{name}, start {guess}: root = {root:.10f}, iterations = {steps}")
    except ValueError as error:
        print(f"{name}, start {guess}: {error}")
