
'''def ContaAluno():
    alunos = []
    cont = 0
    while cont == 0 :
        nomeAluno = input("Digite o seu nome: ")
        sobrenomeAluno = input("digite seu sobrenome: ")
        tamanhoAluno = float(input("Digite seu tamanho"))
        print(nomeAluno)
        print(sobrenomeAluno)
        print(tamanhoAluno)'''

def leLista(n):
    lst=[]
    for i in range(n):
        lst.append(float(input("Digite sua altura: ")))
    return lst

def maiorAltura(lst):
    n = len(lst)
    maior=lst[0]
    for i in range(1,n):
        if lst[i]> maior:
            maior=lst[i]
    return maior

def main():
    qtd = int(input("Digite a qtd de alunos da turma: "))
    lista = leLista(qtd)
    print("A maior altura = %.2f" %(maiorAltura(lista)))

main()

