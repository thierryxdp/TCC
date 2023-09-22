def maiores(lista,n):
    '''
        dada um lista e um inteiro n retorna os valores da lista maiores que n
        lista,int -> list
    '''
    copia=list.copy(lista)
    list.append(copia,n)
    list.sort(copia)
    index=list.index(copia,n)
    return copia[index+1:]