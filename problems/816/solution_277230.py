def maiores(lista,n):
    """essa função retorna todos os números maiores que n dentro de uma lista, caso não haja maiores, a lista retorn vazia;
    list,int->list"""
    list.append(lista,n)
    lista=sorted(lista)
    x=list.index(lista,n)
    y=x+1
    return lista[y:]