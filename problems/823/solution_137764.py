def faltante(lista):
    '''Função que descobre qual intervalo está faltando da lista
    list -> int'''
    list.sort(lista)
    i=0
    while lista[i]==lista[i+1]-1:
        
        i=i+1
    return i