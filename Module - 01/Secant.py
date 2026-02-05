# ---------------- SECANT METHOD ----------------
# Conditions:
# - Generalized: accepts f(x) as input string
# - User enters initial guesses x0, x1
# - Runs exactly 4 iterations
# - Shows formula at start + per iteration substituted formula + result
# - Shows final results of all 4 iterations
# -----------------------------------------------

import math

def make_function(expr: str):
    allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
    allowed["x"] = 0.0

    def f(x):
        allowed["x"] = x
        return eval(expr, {"__builtins__": {}}, allowed)
    return f

def secant_4_iterations():
    print("=== SECANT METHOD FORMULA ===")
    print("x_{k+1} = x_k - f(x_k) * (x_k - x_{k-1}) / ( f(x_k) - f(x_{k-1}) )")
    print("=============================\n")

    expr = input("Enter f(x): ").strip()
    f = make_function(expr)

    x0 = float(input("Enter x0: "))
    x1 = float(input("Enter x1: "))

    results = []

    for i in range(1, 5):
        fx0 = f(x0)
        fx1 = f(x1)
        denom = (fx1 - fx0)

        print(f"Iteration {i}:")

        if denom == 0:
            print("Denominator f(x1)-f(x0) became zero. Cannot continue.\n")
            break

        x2 = x1 - fx1 * (x1 - x0) / denom

        print(f"x{i+1} = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))")
        print(f"     = {x1:.6f} - ({fx1:.6f})*({x1:.6f}-{x0:.6f})/(({fx1:.6f})-({fx0:.6f}))")
        print(f"     = {x2:.6f}\n")

        results.append((x0, x1, x2, f(x2)))

        x0, x1 = x1, x2

    print("Final results of all 4 iterations (x0, x1, x_new, f(x_new)):")
    for k, (A, B, XN, FXN) in enumerate(results, start=1):
        print(f"Iter {k}: x0={A:.6f}, x1={B:.6f}, x_new={XN:.6f}, f(x_new)={FXN:.6f}")

if __name__ == "__main__":
    secant_4_iterations()
