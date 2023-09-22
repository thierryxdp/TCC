def maiores (lista_numeros_inteiros,n):
    media = (sum(lista_numeros_inteiros))/n
    lista_numeros_inteiros.append(media)
    list.sort(lista_numeros_inteiros)
    centro = lista_numeros_inteiros.index(media)
    lista2 = lista_numeros_inteiros[centro:]
    lista2.remove(media)
    return lista2