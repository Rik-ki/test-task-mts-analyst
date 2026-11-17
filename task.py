import math

clicks_a, n_a = 350, 2574
clicks_b, n_b = 375, 2855
p_a = clicks_a / n_a
p_b = clicks_b / n_b

p_pool = (clicks_a + clicks_b) / (n_a + n_b)

se = math.sqrt(p_pool * (1 - p_pool) * (1/n_a + 1/n_b))

z = (p_b - p_a) / se


p_value = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))

print(f"Конверсия A: {p_a:.2%}")
print(f"Конверсия B: {p_b:.2%}")
print(f"z-статистика: {z:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Разница статистически значима")
else:
    print("Разница не статистически значима - оставляем вариант А")