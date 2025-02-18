import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def motion(t, y, mass, mu_s, mu_k, applied_force):
    position, velocity = y
    g = 9.81
    normal_force = mass * g
    
    if np.isclose(velocity, 0):
        max_static_friction = mu_s * normal_force
        if abs(applied_force) <= max_static_friction:
            return [velocity, 0]
        else:
            friction_force = np.sign(applied_force) * max_static_friction
    else:
        friction_force = -np.sign(velocity) * mu_k * normal_force

    net_force = applied_force + friction_force
    acceleration = net_force / mass
    return [velocity, acceleration]

def simulate_friction(mass, mu_s, mu_k, applied_force, t_max=10):
    y0 = [0, 0]
    t_span = (0, t_max)
    t_eval = np.linspace(0, t_max, 500)

    sol = solve_ivp(motion, t_span, y0, t_eval=t_eval, args=(mass, mu_s, mu_k, applied_force), method='RK45')
    return sol.t, sol.y[0], sol.y[1]

def plot_results(t, position, velocity):
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t, position, label='Позиция (М)', color='blue')
    plt.xlabel('Время (С)')
    plt.ylabel('Позиция (М)')
    plt.title('Позиция во времени')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(t, velocity, label='Скорость (М/С)', color='green')
    plt.xlabel('Время (С)')
    plt.ylabel('Скорость (М/С)')
    plt.title('Скорость во времени')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():

    print("Моделирование движения с трением")
    mass = float(input("Введите массу объекта (кг): "))
    mu_s = float(input("Введите коэффициент статического трения: "))
    mu_k = float(input("Введите коэффициент кинетического трения: "))
    applied_force = float(input("Введите приложенную силу (N): "))

    t, position, velocity = simulate_friction(mass, mu_s, mu_k, applied_force)
    plot_results(t, position, velocity)

if __name__ == "__main__":
    main()
