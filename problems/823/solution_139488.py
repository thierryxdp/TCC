def faltante(lista):
    '''Dada uma lista de tamanho n-1 contendo números de 1 a n retorna o número x que pertence ao intervalo [1,n], mas não pertence a lista de entrada
    list -> int'''
    nLista = list(range(len(lista)+1,0,-1))
    c = 0
    while c <= len(lista)+1:
        if c in lista:
            nLista.remove(c)
        c+=1
    return nLista[0]