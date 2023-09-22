def qtd_divisores(n):
    '''Função que dada um inteiro, retorne quantos
    divisores esse número tem;
    Entrada: int
    Saída: int'''
    Qt_d = []
    d = 1
    i = 0
    for elemento in range(1,n+1):
        if n % elemento == 0:
            list.insert(Qt_d,i,elemento)
        d = d+1
        i += 1 
    return len(Qt_d)