def maiores (lista_numeros_inteiros,n):
    media = (sum(lista_numeros_inteiros))/(len(lista_numeros_inteiros))
    lista_numeros_inteiros.append(media)
    list.sort(lista_numeros_inteiros)
    centro = lista_numeros_inteiros.index(media)
    lista2 = lista_numeros_inteiros[centro:]
    lista3 = lista2.remove(centro)
    return lista3