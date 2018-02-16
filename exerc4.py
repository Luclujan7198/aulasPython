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
    n1 = int(input("primeiro numero: "))
    n2 = int(input("segundo numero: "))
    for i in range(n1,n2 + 1):
        if contaNumeroPrimo(i):
            print("%d é primo " %i)
        else:
            print("%d não é primo " %i)

Main()