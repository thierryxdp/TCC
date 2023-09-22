def maiores(lista,n):
    '''retorna uma lista com todos os numeros da lista de numeros
    inteiros original que são maiores que um numero n;
    list,int->list'''
    list.append(lista,n)
    list.sort(lista)
    pos=list.index(lista,n)
    return lista[pos+1:]