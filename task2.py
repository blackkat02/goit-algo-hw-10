import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi


# Побудова графіка функції
# Визначення функції та межі інтегрування
def f(x):
    return x ** 2 + 5 * x + 7

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()
# Малювання функції
ax.plot(x, y, 'r', linewidth=2)
# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 + 5x + 7 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


# Перевірка результатів за допомогою аналітичних розрахунків та функції quad
# Обчислення інтегралу методом Монте-Карло
def monte_carlo_integration(f, a, b, num_points=10000):
    total_area = 0
    for _ in range(num_points):
        x = random.uniform(a, b)
        y = f(x)
        total_area += y
    average_height = total_area / num_points
    return (b - a) * average_height


# Обчислення площі методом Монте-Карло
approx_area = monte_carlo_integration(f, a, b)
print(f"Обчислена площа методом Монте-Карло: {approx_area}")


# Аналітичне обчислення інтегралу
result, error = spi.quad(f, a, b)
print("Аналітичний інтеграл:", result)
print("Похибка:", error)
