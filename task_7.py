import random
from collections import Counter
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_simulations):
    sums = [random.randint(1, 6) + random.randint(1, 6) for _ in range(num_simulations)]

    counts = Counter(sums)

    print(f"{'Сума':<6} | {'Кількість':<10} | {'Ймовірність (Монте-Карло)':<25} | {'Теоретична ймовірність':<25}")
    print("-" * 75)

    for sum_val in range(2, 13):
        count = counts.get(sum_val, 0)
        probability = (count / num_simulations) * 100
        
        # Theoretical probability
        theoretical_combinations = 6 - abs(sum_val - 7)
        theoretical_prob = (theoretical_combinations / 36) * 100
        print(f"{sum_val:<6} | {count:<10} | {f'{probability:.2f}%':<25} | {f'{theoretical_prob:.2f}%':<25}")

    return counts


rolls = 1000000
counts = simulate_dice_rolls(rolls)

sums = list(range(2, 13))
probs = [(counts[s] / rolls) * 100 for s in sums]

bars = plt.bar(sums, probs, color='skyblue', edgecolor='black')
plt.bar_label(bars, labels=[f'{p:.2f}%' for p in probs], padding=3)
plt.xlabel('Сума на кубиках')
plt.ylabel('Ймовірність (%)')
plt.title(f'Ймовірність сум (Монте-Карло: {rolls} кидків)')
plt.xticks(sums)
plt.show()