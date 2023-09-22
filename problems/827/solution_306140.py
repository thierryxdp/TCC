def qtd_divisores(n):
    """função que conta quantos divisores um número tem.
    list -> int"""
    lista = []
    for i in list(range(1,n+1)):
        if n % i == 0:
        	lista.append(i)
    return len(lista)