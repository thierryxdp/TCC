def maiores(lista_numero:list,n:int)->list:
    """Dada uma lista ordenada de números int, inclui n na posição correta, de forma que a lista contuinue ordenada."""
    lista_numero.append(n)
    lista_numero.sort()
    num = lista_numero.index(n)
    del lista_numero[0:num+1]
    return lista_numero