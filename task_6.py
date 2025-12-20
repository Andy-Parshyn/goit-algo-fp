class Item:
    def __init__(self,name,cost,calories):
        self.cost = cost
        self.calories = calories
        self.rate = cost/calories
        self.name = name

def greedy(items: list[Item], budget:int):
    items.sort(key=lambda x : x.rate, reverse=True)
    total_calories = 0
    result = []
    for item in items:
        if budget >= item.cost:
            budget -= item.cost
            total_calories += item.calories
            result.append(item.name)
    return result, total_calories

def dynamic(items: list[Item], budget:int):
    count = len(items)
    K = [[0 for _ in range(budget + 1)] for _ in range(count + 1)]

    for i in range(count + 1):
        for c in range(budget +1 ):
            if i == 0 or c == 0:
                K[i][c] = 0
            elif items[i-1].cost <= c:
                K[i][c] = max(items[i-1].calories + K[i - 1][c - items[i-1].cost],K[i - 1][c])
            else:
                K[i][c] = K[i - 1][c]
    
    max_calories = K[count][budget]
    
    # To display better results
    c = budget
    selected_items = []
    
    for i in range(count, 0, -1):
        if K[i][c] != K[i-1][c]:
            selected_items.append(items[i-1].name)
            c -= items[i-1].cost
    
    selected_items.reverse()  
    
    return selected_items, max_calories
    
budget = 74
food_items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

items = [Item(name,data['cost'],data['calories']) for name, data in food_items.items()]


# Greedy Allgorithm
order, result = greedy(items,budget)
print('='*60)
print('"Greedy" Результати: ')
print(f'Обрано наступні предмети: {', '.join(order)}')
print(f'загальна калорійність: {result}')
print('='*60)

# DP Allgorithm
order, result = dynamic(items,budget)
print('"Dynamic Programming" Результати: ')
print(f'Обрано наступні предмети: {', '.join(order)}')
print(f'загальна калорійність: {result}')
print('='*60)
