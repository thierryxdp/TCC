def maiores(lista,n):
    """Função que coloca em ordem crescente uma lista e retira números 
    menores que n.
    list, int->list"""
    list.append(lista,n)
    list.sort(lista)
    x= list.index(lista,n)
    del lista[:x+1]
    return lista