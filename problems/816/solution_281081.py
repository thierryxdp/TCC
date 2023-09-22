def maiores(lista_inteiros,n):
    lista_inteiros.append(n)
    lista_inteiros.sort()
    i=lista_inteiros.index(n)
    return lista_inteiros[i:]