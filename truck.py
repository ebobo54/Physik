import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры системы
total_mass = 10000
friction_coefficient = 0.01
gravity = 9.81
time_step = 0.1
total_time = 20

# Определяем профиль дороги
def road_curvature(x):
    return 5 * np.sin(0.1 * x)

def road_slope(x):
    dx = 1e-3
    return (road_curvature(x + dx) - road_curvature(x)) / dx

# Сила двигателя
def engine_force(t):
    return 5000 if t < 10 else 2000

def simulate():
    position = [0]  # Начальная позиция
    velocity = [60]  # Начальная скорость
    t_values = np.arange(0, total_time + time_step, time_step)

    for t in t_values[:-1]:
        x = position[-1]
        v = velocity[-1]

        slope = road_slope(x)
        weight_force = total_mass * gravity * slope
        friction_force = friction_coefficient * total_mass * gravity
        net_force = engine_force(t) - friction_force - weight_force

        acceleration = net_force / total_mass

        v_new = v + acceleration * time_step
        x_new = x + v_new * time_step

        velocity.append(v_new)
        position.append(x_new)

        print(f"t={t:.2f}, x={x_new:.2f}, v={v_new:.2f}, a={acceleration:.2f}")

    # Проверка на NaN и Infinity после симуляции
    if np.any(np.isnan(position)) or np.any(np.isinf(position)):
        raise ValueError("Positions contain NaN or Infinity values.")

    print(f"Positions: {position}")
    print(f"Velocities: {velocity}")
    return t_values, np.array(position), np.array(velocity)


# Запуск симуляции
time, positions, velocities = simulate()
print(f"Positions before animation: {positions}")

# Графики скорости и положения
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(time, positions, label="Position")
ax1.set_title("Position over Time")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Position (m)")
ax1.grid()
ax1.legend()

ax2.plot(time, velocities, label="Velocity", color="orange")
ax2.set_title("Velocity over Time")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Velocity (m/s)")
ax2.grid()
ax2.legend()

plt.tight_layout()
plt.show()

# Анимация движения
def animate_truck():
    fig, ax = plt.subplots(figsize=(10, 5))

    if len(positions) == 0:
        raise ValueError("Positions array is empty.")

    ax.set_xlim(0, max(positions) * 1.1)
    ax.set_ylim(-10, 10)  # увеличено до -10, 10

    road_x = np.linspace(0, max(positions), 500)
    road_y = road_curvature(road_x)
    ax.plot(road_x, road_y, label="Road", color="gray")

    truck, = ax.plot([], [], 'ro', label="Truck")
    
    def init():
        truck.set_data([], [])
        return truck,

    def update(frame):
        x = positions[frame]
        y = road_curvature(x)
        truck.set_data(x, y)
        return truck,

    ani = FuncAnimation(fig, update, frames=len(positions), init_func=init, blit=True, interval=50)
    plt.legend()
    plt.title("Truck Animation")
    plt.show()

animate_truck()
