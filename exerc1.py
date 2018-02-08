import random

def leListaInteiros(n):
    lst=[]
    for i in range(n):
        lst.append(random.randint(0,100))
    return lst

def somaLista(lst):
    soma=0
    for i in range(len(lst)):
        soma = soma + lst[i]
    return soma

def Main():
    qtd = int(input("Digite a qtd de elementos: "))
    lista = leListaInteiros(qtd)
    print(lista)
    print("A media = %.2f" %(somaLista(lista)/qtd))

Main()