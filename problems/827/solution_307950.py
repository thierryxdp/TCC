import math 
def qtd_divisores(n):
    '''Função que retorna a quantidade de divisores de um numero 
    dado na entrada n
    int -> int'''
    divisores = [1]
    if n <= 0:
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            divisores.extend([i,n/i])
    divisores.extend([n])
    lista = list (set(divisores))
    return len(lista)