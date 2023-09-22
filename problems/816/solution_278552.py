def maiores(lista,n):
    '''
    dado uma lista e um numero inteiro n
    retorna outra lista com todos os numeros maiores que n
    entrada:lista,int
    saida:lista
    '''
    lista[0:0]=[n]
    list.sort(lista)
    x=list.index(lista,n)
    lista=lista[:x]
    return lista