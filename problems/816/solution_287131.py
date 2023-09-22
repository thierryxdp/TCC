def maiores(lista_inteiros,n):
    """retorna uma lista que contem apenas os elementos
    maiores que n ordenados em ordem crescente.
    list, int -> list"""
    nova_lista = lista_inteiros[:]
    nova_lista.append(n)
    nova_lista.sort()
    indice = nova_lista.index(n)
    ocorrencias = nova_lista.count(n)
    if ocorrencias < 1:
        del nova_lista[:indice+1]
    else:
        del nova_lista[:indice+ocorrencias]
    return nova_lista