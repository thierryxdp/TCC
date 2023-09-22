def maiores(lista,n):
    '''Função que dado uma lista de numeros inteiros e um numero n retorna
    uma lista com os numeros maiores que n;
    list,int-> list'''
    list.sort(lista)
    x= list.index(lista,n)
    return lista[x+1:]