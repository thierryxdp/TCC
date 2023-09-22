def faltante(lista):
    '''A função retorna o número faltante da peça de Joãozinho
    lista -> int'''
    
    i = 0
    x = len(lista)
    y = [] #numero inteiro que percence ao intervalo [1,N]
    
    
    while i < x:
        if lista[i] != i+1:
            list.extend(y,[i+1])
        i = i + 1
    return y[0]