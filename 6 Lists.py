from pyparsing import null_debug_action


demo_list = [1, "Gerardo", "Gato", 459.3]
colors = ["red", "green", "blue"]

numbers_list = list((1,2,3,4))
print(numbers_list)

r = list(range(1,10))
print(r)

print(colors[1])

print('green' in colors)
print(colors)
colors[1] = "yellow"
print(colors)

#print(dir(colors))
colors.append("beige")
colors.extend(("violet","black"))
colors.insert(0,"navy blue")
colors.insert(len(colors),"Brown")
print(colors)
colors.pop() #elimina el último elemento de una lista
print(colors)
colors.remove("yellow")
print(colors)
colors.pop(3)
print(colors)
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)
print(colors.index("black"))
print(colors.count("black"))