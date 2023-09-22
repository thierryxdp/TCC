""" Função que dado um número n qualquer, retorna uma lista contendo a quantidade dos divisores desse numero
int->lista"""

def qtd_divisores(n):
    divisores=[]
    for i in range(1,n+1):
        if n%i==0:
            divisores.append(i)
    return len(divisores)