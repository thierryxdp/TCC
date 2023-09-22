def filtraMultiplos(lista,n):
    '''Função que recebe de entrada uma lista e um numero, e
    retorna uma lista''' 
    l = []
    indice = -1
    while lista[indice]%n==0:
        list.append(l,lista[indice])
        indice = indice-1
        return l