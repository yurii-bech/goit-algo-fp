def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    chosen_items = []
    total_cost = 0
    total_calories = 0

    for item_name, item_info in sorted_items:
        if total_cost + item_info['cost'] <= budget:
            chosen_items.append(item_name)
            total_cost += item_info['cost']
            total_calories += item_info['calories']

    return chosen_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            item_name = list(items.keys())[i - 1]
            cost = items[item_name]['cost']
            calories = items[item_name]['calories']

            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)

    chosen_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name = list(items.keys())[i - 1]
            chosen_items.append(item_name)
            j -= items[item_name]['cost']

    chosen_items.reverse()
    return chosen_items, dp[n][budget]

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Виклик функцій та вивід результатів
greedy_chosen_items, greedy_total_calories = greedy_algorithm(items, budget)
print(f"Greedy Algorithm: Chosen items: {greedy_chosen_items}, Total Calories: {greedy_total_calories}")

dp_chosen_items, dp_total_calories = dynamic_programming(items, budget)
print(f"Dynamic Programming: Chosen items: {dp_chosen_items}, Total Calories: {dp_total_calories}")