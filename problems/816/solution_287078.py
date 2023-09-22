def maiores(lista_numero,n):
    """Retorne uma lista crescente com todos os numeros maiores que n;
    list, int - > list"""
    lista_numero += [n,]
    lista_numero.sort()
    indice = lista_numero.index(n)
    lista = lista_numero[indice+1:]
    return lista