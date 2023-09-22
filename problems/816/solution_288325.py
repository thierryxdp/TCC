def maiores(lista,n):
    ''' funcao que recebe uma lista e um int, e retorna outra lista com todos os numeros maiores em forma crescente '''
    list.insert(lista,0,n)
    list.sort(lista)
    return lista[list.index(lista,n)+1:]