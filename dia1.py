def maximo(a, b):
    if (a > b):
        return a
    elif (b > a):
        return b
    return 'São Iguais'

def multiplo(a, b):
    if (a % b == 0):
        return True
    return False

def SquareArea(a):
    area = a^2
    return area


num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))

print(maximo(num1, num2))
print(multiplo(num1, num2))

lado = int(input("Informe o numero de lados: "))

print(SquareArea(lado))
