from ast import Num


def hello(name = "Person"):
    print("Hello " + name)

#hello("Paty")
hello()

def addition (numberOne, numbertwo):
    return numberOne + numbertwo

print(addition(3,5))

addition_w_lambda = lambda numberOne, numberTwo: numberOne + numberTwo

print(addition_w_lambda(5,2))
