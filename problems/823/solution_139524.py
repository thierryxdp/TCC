def faltante(lista):
    '''Retorna o número N que está faltando na lista de N-1 termos.
    lista -> int'''

    n = len(lista) +1

    while n >0:
        if not n in lista:
            return n

        n = n-1