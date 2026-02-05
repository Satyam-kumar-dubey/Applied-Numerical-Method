# ---------------- GAUSS SEIDEL (3x3) ----------------
# Requirements covered:
# - Generalized for 3 equations input
# - Accepts equations (coefficients + RHS)
# - Runs exactly 4 iterations
# - Shows formulas at start + substituted formula each iteration
# - Prints all 4 iteration results
# ----------------------------------------------------

def read_system_3x3():
    print("Enter coefficients and RHS for 3 equations in the form:")
    print("a11 a12 a13 b1")
    print("a21 a22 a23 b2")
    print("a31 a32 a33 b3")
    A = []
    b = []
    for i in range(3):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != 4:
            raise ValueError("Each row must have 4 numbers: a1 a2 a3 b")
        A.append(row[:3])
        b.append(row[3])
    return A, b

def gauss_seidel_3x3(A, b, x0=(0.0, 0.0, 0.0), iterations=4):
    a11,a12,a13 = A[0]
    a21,a22,a23 = A[1]
    a31,a32,a33 = A[2]
    b1,b2,b3 = b

    if a11 == 0 or a22 == 0 or a33 == 0:
        raise ZeroDivisionError("Diagonal element is zero; Seidel needs non-zero diagonal.")

    print("\n=== GAUSS SEIDEL FORMULAS ===")
    print("Uses latest available updates in the same iteration:")
    print("x1^(k+1) = (b1 - a12*x2^(k)   - a13*x3^(k))   / a11")
    print("x2^(k+1) = (b2 - a21*x1^(k+1) - a23*x3^(k))   / a22")
    print("x3^(k+1) = (b3 - a31*x1^(k+1) - a32*x2^(k+1)) / a33")
    print("=============================\n")

    x1, x2, x3 = x0
    results = []

    print(f"Initial guess: x1^0={x1:.6f}, x2^0={x2:.6f}, x3^0={x3:.6f}\n")

    for k in range(iterations):
        print(f"Iteration {k+1}:")

        # Update x1 using old x2, x3
        new_x1 = (b1 - a12*x2 - a13*x3) / a11
        print(f"x1^{k+1} = ({b1:.6f} - ({a12:.6f})*({x2:.6f}) - ({a13:.6f})*({x3:.6f})) / ({a11:.6f}) = {new_x1:.6f}")

        # Update x2 using new_x1 and old x3
        new_x2 = (b2 - a21*new_x1 - a23*x3) / a22
        print(f"x2^{k+1} = ({b2:.6f} - ({a21:.6f})*({new_x1:.6f}) - ({a23:.6f})*({x3:.6f})) / ({a22:.6f}) = {new_x2:.6f}")

        # Update x3 using new_x1 and new_x2
        new_x3 = (b3 - a31*new_x1 - a32*new_x2) / a33
        print(f"x3^{k+1} = ({b3:.6f} - ({a31:.6f})*({new_x1:.6f}) - ({a32:.6f})*({new_x2:.6f})) / ({a33:.6f}) = {new_x3:.6f}")
        print()

        x1, x2, x3 = new_x1, new_x2, new_x3
        results.append((x1, x2, x3))

    print("Final results of all 4 iterations:")
    for i, (r1, r2, r3) in enumerate(results, start=1):
        print(f"Iter {i}: x1={r1:.6f}, x2={r2:.6f}, x3={r3:.6f}")

    return results

if __name__ == "__main__":
    A, b = read_system_3x3()
    print("\nEnter initial guess x1 x2 x3 (or press Enter for 0 0 0):")
    s = input("x1 x2 x3: ").strip()
    if s:
        x0 = tuple(map(float, s.split()))
        if len(x0) != 3:
            raise ValueError("Initial guess must have 3 numbers.")
    else:
        x0 = (0.0, 0.0, 0.0)

    gauss_seidel_3x3(A, b, x0=x0, iterations=4)
