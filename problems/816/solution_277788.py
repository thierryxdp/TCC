def maiores(lista,n):
    """Retorna uma lista com números maiores que n.
    Parametros:
    Entrada:list,int
    Saida:list"""
    list.append(lista,n)
    list.sort(lista)
    index=list.index(lista,n)
    lista=lista[index+1:]
    return lista