import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Визначення змінних
Lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість Лимонаду
FruitJuice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')  # Кількість Фруктового соку

# Функція цілі (Максимізація загальної кількості вироблених продуктів)
model += Lemonade + FruitJuice, "Total Production"

# Додавання обмежень
model += 2 * Lemonade + 1 * FruitJuice <= 100  # Обмеження на Воду
model += 1 * Lemonade <= 50  # Обмеження на Цукор
model += 1 * Lemonade <= 30  # Обмеження на Лимонний сік
model += 2 * FruitJuice <= 40  # Обмеження на Фруктове пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти Лимонаду:", Lemonade.varValue)
print("Виробляти Фруктового соку:", FruitJuice.varValue)
