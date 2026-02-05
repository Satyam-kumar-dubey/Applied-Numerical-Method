# ---------------- NEWTON-RAPHSON METHOD ----------------
# Conditions:
# - Generalized: accepts f(x) and f'(x) as input strings
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

def newton_raphson_4_iterations():
    print("=== NEWTON-RAPHSON FORMULA ===")
    print("x_{k+1} = x_k - f(x_k)/f'(x_k)")
    print("================================\n")

    fexpr = input("Enter f(x): ").strip()
    dfexpr = input("Enter f'(x): ").strip()

    f = make_function(fexpr)
    df = make_function(dfexpr)

    x = float(input("Enter initial guess x0: "))

    results = []

    for i in range(1, 5):
        fx = f(x)
        dfx = df(x)

        print(f"Iteration {i}:")

        if dfx == 0:
            print("f'(x) became zero. Cannot continue.\n")
            break

        x_new = x - fx / dfx

        print(f"x{i} = x{i-1} - f(x{i-1})/f'(x{i-1})")
        print(f"   = {x:.6f} - ({fx:.6f})/({dfx:.6f})")
        print(f"   = {x_new:.6f}\n")

        results.append((x, fx, dfx, x_new))
        x = x_new

    print("Final results of all 4 iterations (x_old, f(x_old), f'(x_old), x_new):")
    for k, (xo, fxo, dfxo, xn) in enumerate(results, start=1):
        print(f"Iter {k}: x_old={xo:.6f}, f={fxo:.6f}, f'={dfxo:.6f}, x_new={xn:.6f}")

if __name__ == "__main__":
    newton_raphson_4_iterations()
