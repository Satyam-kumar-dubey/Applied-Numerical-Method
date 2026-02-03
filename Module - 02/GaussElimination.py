import numpy as np

# System:
# 41x - 2y + 7z = 81
#  x -27y + 4z = 65
#  x + 5y +50z = 172

A = np.array([
    [41, -2,  7],
    [ 1, -27, 4],
    [ 1,  5, 50]
], dtype=float)

b = np.array([81, 65, 172], dtype=float)


def print_aug(M, title=None):
    if title:
        print(title)
    for row in M:
        print("  " + " ".join(f"{v:12.6f}" for v in row))
    print()


def gauss_elimination_with_steps(A, b, show_steps=4):
    print("GAUSS ELIMINATION")
    print("=================\n")
    print("Idea / Formula:")
    print("  Use row operations to convert [A|b] -> upper triangular [U|c]")
    print("  Then back-substitute to find x, y, z.\n")

    aug = np.hstack([A.copy(), b.reshape(-1, 1)])
    n = aug.shape[0]

    print("Initial augmented matrix [A|b]:")
    print_aug(aug)

    step = 0

    # Forward elimination (partial pivoting)
    for k in range(n - 1):
        pivot_row = k + np.argmax(np.abs(aug[k:, k]))
        if pivot_row != k:
            aug[[k, pivot_row]] = aug[[pivot_row, k]]
            step += 1
            if step <= show_steps:
                print_aug(aug, f"Step {step}: Swap R{k+1} <-> R{pivot_row+1} (pivoting)")

        for i in range(k + 1, n):
            factor = aug[i, k] / aug[k, k]
            aug[i, k:] = aug[i, k:] - factor * aug[k, k:]
            step += 1
            if step <= show_steps:
                print_aug(aug, f"Step {step}: R{i+1} = R{i+1} - ({factor:.6f})*R{k+1}")

    print("After elimination (upper triangular) [U|c]:")
    print_aug(aug)

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        rhs = aug[i, -1] - np.dot(aug[i, i+1:n], x[i+1:n])
        x[i] = rhs / aug[i, i]

    print("Final solution:")
    print(f"  x = {x[0]:.8f}")
    print(f"  y = {x[1]:.8f}")
    print(f"  z = {x[2]:.8f}")
    return x


if __name__ == "__main__":
    gauss_elimination_with_steps(A, b, show_steps=4)
