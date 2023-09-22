def maiores(lista_numeros,n):
    '''Retorna uma lista com todos os inteiros de lista_numeros maiores que n;
    list, int -> list'''
    list.sort(lista_numeros)
    local=list.index(lista_numeros,n)
    return lista_numeros[local+1:]