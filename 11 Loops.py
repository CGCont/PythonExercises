foods = ['apples', 'bread', 'cheese', 'milk']

for food in foods:
    if food == 'cheese':
        print("You need to buy this")
        break
    print(food)

for food in foods:
    if food == 'cheese':
        print("You need to buy this")
        continue #saltar el valor de cheese
    print(food)

