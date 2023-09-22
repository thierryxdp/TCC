def maiores(lista_numeros,n):
    """Essa função retorna uma lista com os números maiores que n.
    Como entrada temos uma lista de números e um valor inteiro n, e
    como saída temos uma lista nova com os números maiores que n
    list,int->list"""
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    if lista_numeros[0]==n:
        list.remove(lista_numeros,n)
        return lista_numeros
    if lista_numeros[len(lista_numeros)-1]==n :
        lista=[]
        return lista
    else:
        indice=list.index(lista_numeros,n)
        del lista_numeros[:indice+1]
        return lista_numeros