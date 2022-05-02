from cgi import print_arguments


myStr = "Hello world"

#print (dir(myStr)) #Muestra las acciones que se pueden realizar
print(myStr.upper()) #Convierte el texto a mayusculas
print(myStr.lower()) #Texto a minusculas
print(myStr.swapcase()) #Primera letra en minuscula el resto en mayusculas
print(myStr.capitalize()) #Primera letra en mayusculas
print(myStr.replace("Hello","Bye")) #Reemplkazar texto
print(myStr.replace("Hello","Bye").upper()) #Anidación de funciones
print(myStr.count("l")) #Contar caracteres
print(myStr.startswith("Hola")) #verificar si un texto comienza con..
print(myStr.startswith("H")) #verificar si un texto comienza con..
print(myStr.endswith("ld")) #verificar si un texto termina con..
print(myStr.split("o")) #dividir un texto
print(myStr.find("o")) #Buscar la posición de una letra
print(len(myStr)) #Longitud de un texto
print(myStr.index("e")) #obtener el indice de un caracter
print(myStr.isnumeric()) #verificar si la variable es numérica
print(myStr[4]) #imprimir el indice de una cadena
print(myStr[-1]) #Obtener caracter inverso

#Distintas formas de imprimir en pantalla
print ("This is " + myStr) 
print(f"This is {myStr}")
print("This is {0}".format(myStr))
