def qtd_divisores (num):
    """retorna a quantidade de divisores que um número possui.
int -> int"""
    soma = 0
    for i in range(1,num+1):
        if num % i == 0:
            soma = soma + 1 
    return soma