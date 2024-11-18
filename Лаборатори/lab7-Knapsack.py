def fractional_knapsack(values, weights, capacity):
    # Нэгж жингийн үнэлгээг тооцоолох
    items = [(v, w, v / w) for v, w in zip(values, weights)]
    # Үнэлгээгээр эрэмбэлэх
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0  # Нийт үнэ
    for value, weight, ratio in items:
        if capacity >= weight:
            # Бүхэлд нь авна
            capacity -= weight
            total_value += value
        else:
            # Хэсэгчлэн авна
            total_value += capacity * ratio
            break
    
    return total_value

# Жишээ өгөгдөл
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(f"Нийт үнэ: {fractional_knapsack(values, weights, capacity)}")
