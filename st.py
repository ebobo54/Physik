# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# m1, m2 = 2.0, 1.0
# v1_init, v2_init = 3.0, -1.0
# x1, x2 = 0.0, 5.0
# collision_type = 'elastic'
# dt = 0.05


# def elastic_collision(v1, v2, m1, m2):
#     v1_final = (v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2)
#     v2_final = (v2 * (m2 - m1) + 2 * m1 * v1) / (m1 + m2)
#     return v1_final, v2_final

# def inelastic_collision(v1, v2, m1, m2):
#     v_final = (m1 * v1 + m2 * v2) / (m1 + m2)
#     return v_final, v_final

# if collision_type == 'elastic':
#     v1_final, v2_final = elastic_collision(v1_init, v2_init, m1, m2)
# else:
#     v1_final, v2_final = inelastic_collision(v1_init, v2_init, m1, m2)

# fig, ax = plt.subplots()
# ax.set_xlim(-2, 10)
# ax.set_ylim(-1, 1)
# line1, = ax.plot([], [], 'bo', markersize=15, label='Тело 1')
# line2, = ax.plot([], [], 'ro', markersize=15, label='Тело 2')
# ax.legend()

# t_collision = (x2 - x1) / (v1_init - v2_init)
# collision_happened = False

# def init():
#     line1.set_data([], [])
#     line2.set_data([], [])
#     return line1, line2

# def update(frame):
#     global x1, x2, v1_init, v2_init, collision_happened

#     t = frame * dt
#     if not collision_happened and t >= t_collision:
#         v1_init, v2_init = v1_final, v2_final
#         collision_happened = True

#     x1 += v1_init * dt
#     x2 += v2_init * dt

#     line1.set_data([x1], [0])
#     line2.set_data([x2], [0])

#     return line1, line2

# ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=50)
# plt.title(f"Столкновение: {collision_type}")
# plt.grid(True)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m1 = float(input("Масса тела 1 (кг): "))
v1 = float(input("Начальная скорость тела 1 (м/с): "))
m2 = float(input("Масса тела 2 (кг): "))
v2 = float(input("Начальная скорость тела 2 (м/с): "))

x1_0 = -5
x2_0 = 5

v1_curr = abs(v1)
v2_curr = -abs(v2)

dt = 0.01
T = 10
frames = int(T / dt)

x1 = [x1_0]
x2 = [x2_0]

collision_occurred = False

for i in range(1, frames):
    new_x1 = x1[-1] + v1_curr * dt
    new_x2 = x2[-1] + v2_curr * dt

    if not collision_occurred and abs(new_x1 - new_x2) < 0.7:
        v1_after = ((m1 - m2) * v1_curr + 2 * m2 * v2_curr) / (m1 + m2)
        v2_after = ((m2 - m1) * v2_curr + 2 * m1 * v1_curr) / (m1 + m2)
        print(f"Скорость тела 1 после столкновения: {abs(v1_after):.2f} м/с")
        print(f"Скорость тела 2 после столкновения: {abs(v2_after):.2f} м/с\n")
        v1_curr, v2_curr = v1_after, v2_after
        collision_occurred = True

    x1.append(new_x1)
    x2.append(new_x2)

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

line1, = ax.plot([], [], 'ro', markersize=10, label='Тело 1')
line2, = ax.plot([], [], 'bo', markersize=10, label='Тело 2')
ax.legend()

def update(frame):
    line1.set_data([x1[frame]], [0])
    line2.set_data([x2[frame]], [0])
    return line1, line2

ani = FuncAnimation(fig, update, frames=frames, interval=20, blit=True)
plt.title("Упругое столкновение двух тел")
plt.xlabel("Положение (м)")
plt.grid()
plt.show()
