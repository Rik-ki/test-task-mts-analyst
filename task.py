import math

clicks_a, n_a = 350, 2574
clicks_b, n_b = 375, 2855

# Расчёт конверсий
p_a = clicks_a / n_a
p_b = clicks_b / n_b

# Относительная разница конверсий
relative_diff = (p_b - p_a) / p_a

# Объединённая доля для статистического теста
p_pool = (clicks_a + clicks_b) / (n_a + n_b)

# Стандартная ошибка
se = math.sqrt(p_pool * (1 - p_pool) * (1/n_a + 1/n_b))

# Z-статистика
z = (p_b - p_a) / se

# P-value двустороннего z-теста
p_value = math.erfc(abs(z) / math.sqrt(2))

print(f"Конверсия A: {p_a:.2%}")
print(f"Конверсия B: {p_b:.2%}")
print(f"Относительная разница (B к A): {relative_diff:.2%}")
print(f"Z-статистика: {z:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05

if p_value < alpha:
    print("Разница статистически значима")
else:
    print("Статистически значимое различие не обнаружено")
