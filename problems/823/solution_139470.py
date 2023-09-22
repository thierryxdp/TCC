def faltante(lista):
    '''Dada uma lista de tamanho n-1 contendo números de 1 a n retorna o número x que pertence ao intervalo [1,n], mas não pertence a lista de entrada
    list -> int'''
    num = 0
    c = 0
    pecas = list(range(max(lista)+1,0,-1))
    while c < len(pecas):
        if c in lista:
            num += c
        c+=1
    return num