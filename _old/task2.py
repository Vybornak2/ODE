# type: ignore
import matplotlib.pyplot as plt
import numpy as np


def system(t, y):
    dxdt = y * (y - 1) * (y + 2)
    dt = np.ones_like(t)
    return dt, dxdt


def main():
    # Define range
    lim = 3
    samples = 200 * lim

    x_range = np.linspace(0, 2 * lim, samples)
    y_range = np.linspace(-lim, lim, samples)

    # Create meshgrid
    X, Y = np.meshgrid(x_range, y_range)

    # Calculate derivatives
    DX, DY = system(X, Y)

    # Create the plot
    plt.figure(figsize=(10, 8))

    # Streamplot for the phase portrait
    # Using a denser grid for streamplot to make it look smoother
    x_dense = np.linspace(0, 2 * lim, samples * 10)
    y_dense = np.linspace(-lim, lim, samples * 10)
    X_dense, Y_dense = np.meshgrid(x_dense, y_dense)
    DX_dense, DY_dense = system(X_dense, Y_dense)

    plt.streamplot(
        X_dense,
        Y_dense,
        DX_dense,
        DY_dense,
        color="blue",
        density=1.5,
        linewidth=1,
        arrowsize=1.5,
    )

    # plt.axvline(x=0, color="red", linestyle="--", alpha=0.5, label="x-nullcline")
    # plt.axvline(x=1, color="red", linestyle="--", alpha=0.5)
    # plt.axvline(x=-1, color="red", linestyle="--", alpha=0.5)
    # plt.axhline(y=0, color="green", linestyle="--", alpha=0.5, label="y-nullcline")

    # fixed_points = [(0, 0), (1, 0), (-1, 0)]
    # for point in fixed_points:
    # plt.plot(
    # point[0],
    # point[1],
    # "ko",
    # markersize=8,
    # label="Fixed Point" if point == fixed_points[0] else "",
    # )

    plt.title(r"Phase Portrait of $\dot{x} = x - x^3, \dot{y} = -y$")
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.xlim(-2, 2)
    # plt.ylim(-2, 2)
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
