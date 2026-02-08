# Copilot Instructions for ODE Repository

## 🎯 Project Goals & Scope
- **Theoretical Focus**: Emphasize the **mathematical theory** behind ODEs (Stability, Topology, Manifolds). Engineering examples should illustrate these concepts.
- **Role of Numerics**: Numerical solutions are tools for **verification**, not the primary goal. Use libraries (`scipy`) to validate symbolic/theoretical findings; avoid implementing solvers manually.
- **Topic Adherence**: Follow the split structure in `README.md`. Use **Practical Exercises** for coding tasks and simulations, and **Theoretical Topics** for mathematical context/definitions. Avoid tangential subjects.
- **Learning & Exploration**: The user is studying. Do not provide "done" solutions. Provide **roadmaps, possibilities, and hints**.

## 🤖 AI Agent Behavior
- **Suggestions > Implementations**:
  - **CRITICAL**: You must **ONLY suggest changes** or strategies. **NEVER implement solutions** or write finished code for the user.
  - Never write the full solution code immediately.
  - Offer **different points of view** or approaches to solving the problem.
  - Highlight key libraries or functions `(e.g., scipy.integrate.solve_ivp)` without writing the full call setup unless requested.
- **Minimalism**:
  - Keep text explanations concise and strictly necessary.
  - Avoid boilerplate.
  - Use bullet points for clarity.

## 📝 Format & Structure
- **Jupyter Notebooks**: Prefer generating content as Logical blocks (Markdown + Code) suitable for Jupyter `.ipynb` files.
  - **Markdown Blocks**: Use extensive markdown to describe the *problem*, *physical context*, and *mathematical formulation* before entering code.
  - **Code Blocks**: Segregate implementation into small, testable cells.
- **Visualization**:
  - "A plot is worth 1000 equations". Always prioritize visual output (Phase portraits, Time series, Vector fields).
  - Use `matplotlib` for clear, engineering-grade plots (labels, grids, legends required).

## 🛠 Tech Stack & Libraries
- **Standard Stack**: Python 3.12+
  - **Symbolic**: `sympy` (derivations, exact solutions) - *Verify results against numerical methods.*
  - **Numerical**: `numpy`, `scipy` (solving, integrating).
- **High Performance (Rust)**:
  - **trigger**: If a specific component is algorithms-heavy, traditionally "black-box" (e.g., custom integrators, intense numerical schemes), or requires high performance.
  - **Action**: Suggest and outline a solution using **Rust** with **PyO3** bindings.
  - *Note*: Only suggest this for the computationally intensive "kernel" of the problem.

## 💡 Example Workflow
1. **Define**: Markdown cell describing the theoretical concept (e.g., "Hartman-Grobman Theorem").
2. **Model**: Markdown cell with LaTeX formulation of the specific system to analyze.
3. **Derive**: Use `sympy` to derive properties (eigenvalues, fixed points) to predict behavior theoretically.
4. **Validate**: Use `scipy` to numerically integrate specific trajectories to confirm theoretical predictions.
5. **Visualize**: Generate a phase portrait to overlay theoretical findings (like nullclines/eigenvectors) on the numerical flow.
