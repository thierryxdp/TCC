def maiores(lista_inteiros,n):
    lista_inteiros.append(n)
    list.sort(lista_inteiros)
    m=lista_inteiros.index(n)
    del(lista_inteiros[:m+1])
    return lista_inteiros