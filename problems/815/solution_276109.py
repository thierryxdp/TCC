def insere(lista_numero, n):
    lista_ordenada = lista_numero.append(n)
    lista_ordenada_final = list.sort(lista_ordenada)
    return lista_ordenada_final