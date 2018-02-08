import random

def leInteiro():
    return (random.randint(0,50))

def contaNumeroPrimo(n):
    contador = 0
    for i in range(1,n+1):
        resto = n % i
        if resto == 0:
            contador = contador + 1

    if contador > 2: 
        return False
    else:
        return True

def Main():
    n = leInteiro()
    if contaNumeroPrimo(n):
        print("%d é primo " %n)
    else:
        print("%d não é primo " %n)

Main()