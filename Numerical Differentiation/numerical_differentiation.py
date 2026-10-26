import numpy as np
import matplotlib.pyplot as plt


# Three methods for estimating a derivative

def FD(f, x, h):
    """Forward difference."""
    return (f(x + h) - f(x)) / h


def CD(f, x, h):
    """Central difference."""
    return (f(x + h / 2) - f(x - h / 2)) / h


def ED(f, x, h):
    """Extrapolated difference using two central differences."""
    return (4 * CD(f, x, h / 2) - CD(f, x, h)) / 3


# Compare the methods with the exact derivative of cos(x)
test_f = np.cos
x0 = 0.1
exact_derivative = -np.sin(x0)
step_sizes = np.logspace(-1, -17, 17)

methods = {"FD": FD, "CD": CD, "ED": ED}
errors = {}

print(f"Derivative of cos(x) at x = {x0}")
print(f"Exact value: {exact_derivative:.12f}\n")
print(f"{'h':>10} {'FD error':>14} {'CD error':>14} {'ED error':>14}")

for name, method in methods.items():
    estimates = [method(test_f, x0, h) for h in step_sizes]
    errors[name] = np.abs((np.array(estimates) - exact_derivative) / exact_derivative)

for i, h in enumerate(step_sizes):
    print(f"{h:10.0e} {errors['FD'][i]:14.4e} {errors['CD'][i]:14.4e} {errors['ED'][i]:14.4e}")

for name in methods:
    best_index = np.argmin(errors[name])
    print(f"{name}: smallest relative error = {errors[name][best_index]:.3e} at h = {step_sizes[best_index]:.0e}")

plt.figure()
for name in methods:
    plt.loglog(step_sizes, errors[name], 'o-', label=name)
plt.xlabel('Step size h')
plt.ylabel('Absolute relative error')
plt.title('Numerical differentiation error vs step size')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Explore subtractive cancellation as h becomes very small
sc_errors = []

for h in step_sizes:
    numerical = (1 + h) - 1
    fractional_error = abs(h - numerical) / h
    sc_errors.append(fractional_error)

plt.figure()
plt.loglog(step_sizes, sc_errors, 'o-', label='Subtractive cancellation')
plt.xlabel('Step size h')
plt.ylabel('Fractional error')
plt.title('Subtractive cancellation vs step size')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
