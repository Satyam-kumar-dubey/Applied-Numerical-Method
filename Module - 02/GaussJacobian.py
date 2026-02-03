# GAUSS–JACOBI METHOD (with formulas per iteration)

def gauss_jacobi(x0=0.0, y0=0.0, z0=0.0, iters=4):
    print("GAUSS–JACOBI METHOD")
    print("===================\n")

    print("Rearranged equations (iteration formulas):")
    print("  x = (81 + 2y - 7z) / 41")
    print("  y = (x + 4z - 65) / 27")
    print("  z = (172 - x - 5y) / 50\n")

    x, y, z = float(x0), float(y0), float(z0)
    print(f"Initial guess:")
    print(f"x(0) = {x:.6f}, y(0) = {y:.6f}, z(0) = {z:.6f}\n")

    for k in range(1, iters + 1):
        print(f"Iteration {k}:")

        print(f"x({k}) = (81 + 2*({y:.6f}) - 7*({z:.6f})) / 41")
        x_new = (81 + 2*y - 7*z) / 41

        print(f"y({k}) = ({x:.6f} + 4*({z:.6f}) - 65) / 27")
        y_new = (x + 4*z - 65) / 27

        print(f"z({k}) = (172 - {x:.6f} - 5*({y:.6f})) / 50")
        z_new = (172 - x - 5*y) / 50

        print(f"Values:")
        print(f"x({k}) = {x_new:.6f}, y({k}) = {y_new:.6f}, z({k}) = {z_new:.6f}\n")

        x, y, z = x_new, y_new, z_new

    print("Approximate solution after 4 iterations:")
    print(f"x ≈ {x:.8f}, y ≈ {y:.8f}, z ≈ {z:.8f}")


if __name__ == "__main__":
    gauss_jacobi(0, 0, 0, 4)
