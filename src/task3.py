# type: ignore
import matplotlib.pyplot as plt
import numpy as np


def system(x, y):
    dxdt = x * (1 - x**2)
    dydt = -y
    return dxdt, dydt


def main():
    # Define range
    lim = 5
    samples = lim * 200
    x_range = np.linspace(-lim, lim, samples)
    y_range = np.linspace(-lim, lim, samples)

    # Create meshgrid
    X, Y = np.meshgrid(x_range, y_range)

    # Calculate derivatives
    DX, DY = system(X, Y)

    # Create the plot
    plt.figure(figsize=(10, 8))

    # Streamplot for the phase portrait
    # Using a denser grid for streamplot to make it look smoother
    x_dense = np.linspace(-lim, lim, samples)
    y_dense = np.linspace(-lim, lim, samples)
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

    # Plot Nullclines
    # x-nullcline: dx/dt = 0 => x = 0, x = 1, x = -1
    plt.axvline(x=0, color="red", linestyle="--", alpha=0.5, label="x-nullcline")
    plt.axvline(x=1, color="red", linestyle="--", alpha=0.5)
    plt.axvline(x=-1, color="red", linestyle="--", alpha=0.5)

    # y-nullcline: dy/dt = 0 => y = 0
    plt.axhline(y=0, color="green", linestyle="--", alpha=0.5, label="y-nullcline")

    # Plot Fixed Points
    # intersection of nullclines: (0,0), (1,0), (-1,0)
    fixed_points = [(0, 0), (1, 0), (-1, 0)]
    for point in fixed_points:
        plt.plot(
            point[0],
            point[1],
            "ko",
            markersize=8,
            label="Fixed Point" if point == fixed_points[0] else "",
        )

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
