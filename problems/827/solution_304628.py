def qtd_divisores(n):
    """Esta função recebe um número inteiro e retorna a quantidade de divisores que este número tem
    int -> int"""
    lista = [ ]
    for i in range(1,n+1):
        if n%i == 0:
            lista.append(i)
    return len(lista)