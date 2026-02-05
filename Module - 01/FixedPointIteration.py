# ---------------- FIXED POINT ITERATION ----------------
# Conditions:
# - Generalized: accepts g(x) as input string
# - User enters initial guess x0
# - Runs exactly 4 iterations
# - Shows formula at start + per iteration substituted formula + result
# - Shows final results of all 4 iterations
# -------------------------------------------------------

import math

def make_function(expr: str):
    allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
    allowed["x"] = 0.0

    def f(x):
        allowed["x"] = x
        return eval(expr, {"__builtins__": {}}, allowed)
    return f

def fixed_point_4_iterations():
    print("=== FIXED POINT ITERATION FORMULA ===")
    print("x_{k+1} = g(x_k)")
    print("A root is achieved when x = g(x).")
    print("=====================================\n")

    gexpr = input("Enter g(x): ").strip()
    g = make_function(gexpr)

    x = float(input("Enter initial guess x0: "))

    results = []

    for i in range(1, 5):
        x_new = g(x)

        print(f"Iteration {i}:")
        print(f"x{i} = g(x{i-1}) = g({x:.6f}) = {x_new:.6f}\n")

        results.append(x_new)
        x = x_new

    print("Final results of all 4 iterations:")
    for k, val in enumerate(results, start=1):
        print(f"Iter {k}: x = {val:.6f}")

if __name__ == "__main__":
    fixed_point_4_iterations()
