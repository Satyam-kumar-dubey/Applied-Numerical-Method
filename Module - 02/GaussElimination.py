# ---------------- GAUSS ELIMINATION (3x3) ----------------
# Requirements covered:
# - Generalized for 3 equations input
# - Shows formulas at start and at each elimination step
# - Outputs 4 stages (Step 1, Step 2, Back-sub stage, Final)
# --------------------------------------------------------

def read_augmented_matrix_3x3():
    print("Enter coefficients and RHS for 3 equations in the form:")
    print("a11 a12 a13 b1")
    print("a21 a22 a23 b2")
    print("a31 a32 a33 b3")
    A = []
    for i in range(3):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != 4:
            raise ValueError("Each row must have 4 numbers: a1 a2 a3 b")
        A.append(row)
    return A  # augmented matrix [A|b], shape 3x4

def print_matrix(M, title="Matrix"):
    print(f"\n{title}:")
    for r in M:
        print("  ", ["{:+.6f}".format(x) for x in r])

def gauss_elimination_3x3(M):
    print("\n=== GAUSS ELIMINATION FORMULAS ===")
    print("We use elimination with multipliers:")
    print("m21 = a21/a11,  R2 <- R2 - m21*R1")
    print("m31 = a31/a11,  R3 <- R3 - m31*R1")
    print("m32 = a32/a22,  R3 <- R3 - m32*R2")
    print("Then back-substitution:")
    print("x3 = a3'/a33',  x2 = (b2' - a23'*x3)/a22',  x1 = (b1' - a12'*x2 - a13'*x3)/a11'")
    print("=================================\n")

    # Copy matrix
    A = [row[:] for row in M]

    # ---------- Step 1: eliminate below pivot a11 ----------
    a11 = A[0][0]
    if a11 == 0:
        raise ZeroDivisionError("Pivot a11 is zero. (This simple version does not do pivoting.)")

    m21 = A[1][0] / a11
    m31 = A[2][0] / a11

    print("STEP 1 (Eliminate a21 and a31 using Row1)")
    print(f"m21 = a21/a11 = ({A[1][0]:.6f})/({a11:.6f}) = {m21:.6f}")
    print(f"R2 <- R2 - m21*R1")
    print(f"m31 = a31/a11 = ({A[2][0]:.6f})/({a11:.6f}) = {m31:.6f}")
    print(f"R3 <- R3 - m31*R1")

    for j in range(4):
        A[1][j] = A[1][j] - m21 * A[0][j]
        A[2][j] = A[2][j] - m31 * A[0][j]

    print_matrix(A, "After Step 1")

    # ---------- Step 2: eliminate below pivot a22 ----------
    a22 = A[1][1]
    if a22 == 0:
        raise ZeroDivisionError("Pivot a22 is zero. (This simple version does not do pivoting.)")

    m32 = A[2][1] / a22

    print("\nSTEP 2 (Eliminate a32 using Row2)")
    print(f"m32 = a32/a22 = ({A[2][1]:.6f})/({a22:.6f}) = {m32:.6f}")
    print("R3 <- R3 - m32*R2")

    for j in range(4):
        A[2][j] = A[2][j] - m32 * A[1][j]

    print_matrix(A, "After Step 2 (Upper triangular)")

    # ---------- Step 3: back substitution start (show formulas) ----------
    print("\nSTEP 3 (Back-substitution formulas with current numbers)")
    a33 = A[2][2]
    b3 = A[2][3]
    a23 = A[1][2]
    b2 = A[1][3]
    a12 = A[0][1]
    a13 = A[0][2]
    b1 = A[0][3]

    if a33 == 0:
        raise ZeroDivisionError("a33 became zero; cannot back-substitute.")

    print(f"x3 = b3'/a33' = ({b3:.6f})/({a33:.6f})")
    x3 = b3 / a33
    print(f"   = {x3:.6f}")

    print(f"x2 = (b2' - a23'*x3)/a22' = ({b2:.6f} - ({a23:.6f})*({x3:.6f}))/({a22:.6f})")
    x2 = (b2 - a23 * x3) / a22
    print(f"   = {x2:.6f}")

    print(f"x1 = (b1' - a12'*x2 - a13'*x3)/a11' = ({b1:.6f} - ({a12:.6f})*({x2:.6f}) - ({a13:.6f})*({x3:.6f}))/({A[0][0]:.6f})")
    x1 = (b1 - a12 * x2 - a13 * x3) / A[0][0]
    print(f"   = {x1:.6f}")

    # ---------- Step 4: final result ----------
    print("\nSTEP 4 (Final Solution)")
    print(f"x1 = {x1:.6f}, x2 = {x2:.6f}, x3 = {x3:.6f}")

    return (x1, x2, x3)

if __name__ == "__main__":
    M = read_augmented_matrix_3x3()
    print_matrix(M, "Initial Augmented Matrix [A|b]")
    gauss_elimination_3x3(M)
