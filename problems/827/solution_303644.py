def qtd_divisores (n):
    """ funcao recebe um numero e retorna quantos divisores este numero tem
    entrada : int saida: int"""
    lista = []
    for i in range (1, n//2+1):
        if n % i == 0:
            list.append (lista,i)
    if len(lista) == 0:
        return len(lista)
    else:
        return len (lista) + 1