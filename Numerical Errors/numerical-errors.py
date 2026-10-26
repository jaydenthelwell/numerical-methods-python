
import math
import sys

import matplotlib.pyplot as plt
import numpy as np


# floating-point precision

epsilon = 0.1

while 1.0 + epsilon != 1.0:
    epsilon /= 2

print("Epsilon rounded away:", epsilon)
print("Machine epsilon:", sys.float_info.epsilon)

print("\n0.1 + 0.2 =", 0.1 + 0.2)
print("Equal to 0.3:", 0.1 + 0.2 == 0.3)
print("Close to 0.3:", math.isclose(0.1 + 0.2, 0.3))


# overflow and underflow

number = 1.0

while math.isfinite(number):
    last_finite = number
    number *= 2

print("\nLargest finite value reached:", last_finite)
print("Maximum finite float:", sys.float_info.max)

number = 10.0**-300
underflow_values = []

while number > 0:
    number /= 300
    underflow_values.append(number)

print("\nRepeated division:")
for value in underflow_values:
    print(f"{value:.3e}")

print("Smallest positive normal float:", sys.float_info.min)
print("Smallest positive subnormal float:", math.nextafter(0.0, 1.0))


# integer overflow

largest_int16 = 2**15 - 1
values = np.array([largest_int16], dtype=np.int16)

print("\nLargest int16:", values[0])
print("After adding one:", np.add(values, np.int16(1)))
print("Python integer after adding one:", largest_int16 + 1)


# subtractive cancellation

def quadratic_direct(a, b, c):
    discriminant = b**2 - 4*a*c
    root_disc = math.sqrt(discriminant)

    x1 = (-b + root_disc) / (2*a)
    x2 = (-b - root_disc) / (2*a)

    return x1, x2


def quadratic_stable(a, b, c):
    discriminant = b**2 - 4*a*c
    root_disc = math.sqrt(discriminant)

    # avoid subtracting nearly equal numbers.
    q = -0.5 * (b + math.copysign(root_disc, b))

    if q == 0:
        return quadratic_direct(a, b, c)

    return q / a, c / q


print("\nSmall root comparison")
print(f"{'c':>12} {'Direct':>20} {'Stable':>20}")

for n in range(1, 17):
    c = 10.0**(-n)

    direct_root = min(quadratic_direct(1, 1, c), key=abs)
    stable_root = min(quadratic_stable(1, 1, c), key=abs)

    print(f"{c:12.1e} {direct_root:20.12e} {stable_root:20.12e}")


# check how closely the calculated roots satisfy the equation.

a, b, c = 1.0, 1.0, 1e-12

for method in (quadratic_direct, quadratic_stable):
    roots = method(a, b, c)
    residuals = [a*x**2 + b*x + c for x in roots]

    print(f"\n{method.__name__}:")
    print("Roots:", roots)
    print("Residuals:", residuals)


# taylor series approximation for sin(x)

def sine_sum(x, tolerance=1e-15, max_terms=1000):
    total = x
    term = x
    n = 1

    while abs(term) > tolerance and n < max_terms:
        term *= -(x**2) / ((2*n) * (2*n + 1))
        total += term
        n += 1

    return total


x = 2.0
approximation = sine_sum(x)

print("\nTaylor approximation:", approximation)
print("math.sin:", math.sin(x))
print("Absolute error:", abs(approximation - math.sin(x)))


# compare the approximation with NumPy over a range of inputs.


x_values = np.linspace(-2 * np.pi, 2 * np.pi, 400)
approximation = np.array([sine_sum(x) for x in x_values])
exact = np.sin(x_values)
error = np.abs(approximation - exact)

plt.plot(x_values, approximation, label="Taylor series")
plt.plot(x_values, exact, "--", label="NumPy sin")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.semilogy(x_values, np.maximum(error, 1e-18))
plt.xlabel("x")
plt.ylabel("Absolute error")
plt.grid(True)
plt.tight_layout()
plt.show()

print("Maximum absolute error:", error.max())
