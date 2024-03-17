import random

def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}  # Створюємо словник для підрахунку кількості кожної суми
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)  # Кидаємо перший кубик
        dice2 = random.randint(1, 6)  # Кидаємо другий кубик
        total_sum = dice1 + dice2  # Обчислюємо суму чисел, які випали
        sums_count[total_sum] += 1  # Збільшуємо лічильник для відповідної суми
    return sums_count

num_rolls = 100000  # Кількість кидків для симуляції
results = simulate_dice_rolls(num_rolls)

# Розрахунок ймовірностей кожної суми
probabilities = {key: value / num_rolls * 100 for key, value in results.items()}

# Вивід результатів у вигляді таблиці
print("Сума\tІмовірність")
for key, value in probabilities.items():
    print(f"{key}\t{value:.2f}% ({results[key]} / {num_rolls})")