
import numpy as np
import matplotlib.pyplot as plt


# Bisection method

def bisection_step(f, bounds):
    lower, upper = bounds
    middle = (lower + upper) / 2

    if f(lower) == 0:
        return lower, lower
    if f(upper) == 0:
        return upper, upper

    if f(lower) * f(middle) < 0:
        return lower, middle
    else:
        return middle, upper


def bisection_algorithm(f, bounds, tolerance=1e-10):
    lower, upper = bounds

    if f(lower) * f(upper) > 0:
        raise ValueError("The interval must bracket a root.")

    iterations = 0

    while upper - lower > tolerance:
        lower, upper = bisection_step(f, (lower, upper))
        iterations += 1

    root = (lower + upper) / 2
    return root, iterations


# Regula falsi method

def regula_falsi_step(f, bounds):
    lower, upper = bounds
    fl, fu = f(lower), f(upper)

    middle = (lower * fu - upper * fl) / (fu - fl)

    if fl * f(middle) < 0:
        return lower, middle
    else:
        return middle, upper


def regula_falsi(f, bounds, tolerance=1e-8, max_iterations=10000):
    lower, upper = bounds

    if f(lower) * f(upper) > 0:
        raise ValueError("The interval must bracket a root.")

    iterations = 0

    while abs(f(lower)) >= tolerance and abs(f(upper)) >= tolerance:
        if iterations >= max_iterations:
            raise ValueError("Regula falsi did not converge.")

        lower, upper = regula_falsi_step(f, (lower, upper))
        iterations += 1

    root = lower if abs(f(lower)) < abs(f(upper)) else upper
    return root, iterations


# Test functions

def f(x):
    return x**2 - 4


def g(x):
    return x**8 - 2*x - 1


def h(x):
    return (x - 1) / (x - 2)


def j(x):
    return x**3 + 47*x**2 - 148*x + 90


# Compare the two methods for x^2 - 4

print("Finding a root of x^2 - 4")

bisection_root, bisection_iterations = bisection_algorithm(f, (0, 5))
false_position_root, false_position_iterations = regula_falsi(f, (0, 5))

print("Bisection:")
print("Root:", bisection_root)
print("Iterations:", bisection_iterations)
print("Function value:", f(bisection_root))

print("\nRegula falsi:")
print("Root:", false_position_root)
print("Iterations:", false_position_iterations)
print("Function value:", f(false_position_root))


# Try the methods on other functions

print("\nTrying other functions")

for function, interval in [(g, (0, 5)), (h, (0, 1.5)), (j, (2, 3))]:
    print(f"\nFunction: {function.__name__}")

    try:
        root, iterations = bisection_algorithm(function, interval)
        print("Bisection:", root, "Iterations:", iterations)
    except ValueError as error:
        print("Bisection:", error)

    try:
        root, iterations = regula_falsi(function, interval)
        print("Regula falsi:", root, "Iterations:", iterations)
    except ValueError as error:
        print("Regula falsi:", error)


# Plot the first test function

x = np.linspace(0, 5, 200)
y = f(x)

plt.plot(x, y, label="f(x) = x² - 4")
plt.axhline(0, linewidth=0.8)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Finding roots using numerical methods")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
