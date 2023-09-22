def faltante(listaLN):
    '''Função que recebe uma lista de números inteiros e descobre
    qual número está faltando no intervalo
    tipo de entrada: list
    tipo de saída: int'''
    
    a = [0] + listaLN + [0]
    b = 0
    c = list(range(len(listaLN)+1)) + [listaLN] + [0]
    
    while b <= len(a):
        if c[b] != a[b]:
            return a[b-1]+1
        t += 1