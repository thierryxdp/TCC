def maiores (lista_numeros_inteiros,n):
    lista_numeros_inteiros.append(n)
    list.sort(lista_numeros_inteiros)
    centro = lista_numeros_inteiros.index(n)
    lista2 = lista_numeros_inteiros[centro:]
    lista2.remove(n)
    return lista2