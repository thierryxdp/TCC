def qtd_divisores(n):
    '''Função que dada um inteiro, retorne quantos
    divisores esse número tem.
    Entrada: int
    Saída: int'''
    D = []
    d = 1
    for numero in range(1,n):
        if numero % d == 0:
            list.insert(D,0,d)
        d += 1
    return D