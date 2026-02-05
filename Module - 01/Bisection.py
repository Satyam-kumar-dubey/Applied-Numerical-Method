# ---------------- BISECTION METHOD ----------------
# Conditions:
# - Generalized: accepts f(x) as input string
# - User enters interval [a,b]
# - Runs exactly 4 iterations
# - Shows formula at start + per iteration substituted formula + result
# - Shows final results of all 4 iterations
# --------------------------------------------------

import math

def make_function(expr: str):
    allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
    allowed["x"] = 0.0

    def f(x):
        allowed["x"] = x
        return eval(expr, {"__builtins__": {}}, allowed)
    return f

def bisection_4_iterations():
    print("=== BISECTION METHOD FORMULA ===")
    print("Given [a,b] such that f(a)*f(b) < 0:")
    print("c = (a + b)/2")
    print("If f(a)*f(c) < 0 => b = c else a = c")
    print("================================\n")

    expr = input("Enter f(x): ").strip()
    f = make_function(expr)

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))

    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("\nWARNING: f(a)*f(b) > 0. Bisection may not be valid for this interval.\n")

    results = []

    for i in range(1, 5):
        c = (a + b) / 2.0
        fa = f(a)
        fb = f(b)
        fc = f(c)

        print(f"Iteration {i}:")
        print(f"c{i} = (a + b)/2 = ({a:.6f} + {b:.6f})/2 = {c:.6f}")
        print(f"f(a) = {fa:.6f}, f(c{i}) = {fc:.6f}, f(b) = {fb:.6f}")

        # update interval
        if fa * fc < 0:
            print("Since f(a)*f(c) < 0 => root in [a, c], so b = c\n")
            b = c
        else:
            print("Else root in [c, b], so a = c\n")
            a = c

        results.append((a, b, c, fc))

    print("Final results of all 4 iterations (a, b, c, f(c)):")
    for k, (A, B, C, FC) in enumerate(results, start=1):
        print(f"Iter {k}: a={A:.6f}, b={B:.6f}, c={C:.6f}, f(c)={FC:.6f}")

if __name__ == "__main__":
    bisection_4_iterations()
