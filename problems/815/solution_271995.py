def insere(lista_numeros,n):
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    objeto=list.index(lista_numeros,n)
    lista_numeros=lista_numeros[objeto+1:]
    return lista_numeros