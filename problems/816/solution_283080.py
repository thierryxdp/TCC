# retorna uma lista em que todos os números de uma lista de origem são maiores que n, em ordem crescente
def maiores(lista,n):
    lista.append(n)
    lista.sort()
    lista = lista[lista.index(n)+ 1:]
    return lista