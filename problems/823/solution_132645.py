def faltante(lista):
    '''A função retorna o número faltante da peça de Joãozinho
    lista -> int'''
    
    i = 0
    x = len(lista)
    lista = [] #numero inteiro que percence ao intervalo [1,N]
    
    
    while i < x:
        if lista[i] != i+1:
            list.extend(lista,i)
        i = i + 1
    return lista