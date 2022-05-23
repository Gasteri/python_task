day_sales = [1589.5, 2687.5, 5478.2, 1236.5, 4756.5]
idx = 0
total_sales = 0
while idx < len(day_sales):
    total_sales = total_sales + day_sales[idx]
    idx = idx + 1
price_per_product = total_sales / len(day_sales)
print(price_per_product)

day_sales = [1589.5, 2687.5, 5478.2, 1236.5, 4756.5]
total_sales = 0
for product_price in day_sales:
    total_sales += product_price
price_per_product = total_sales / len(day_sales)
print(price_per_product)

day_sales = [1589.5, 2687.5, 5478.2, 1236.5]
discount = 5
for idx in range(len(day_sales)):
    day_sales[idx] *= (100 - discount) / 100
print(day_sales)


day_sales = [1589.5, 2687.5, 5478.2, 1236.5, 4756.5]
for idx, item in enumerate(day_sales, start=1):
    print('товар №', idx, '-', item)vvv