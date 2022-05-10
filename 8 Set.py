colors = {
    "green", "red", "yellow", "black"
}

print( type ( colors ) )

print (colors)

print( "red" in colors ) #Imprime si red esta en la colección colors

colors.add ("purple")
print(colors)
colors.remove("red")
print(colors)
colors.clear
print(colors)
del colors #elimmina el set