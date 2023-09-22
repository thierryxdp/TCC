def insere(lista_numero,n):
    lista= lista_numero
    numero_inserido= list.insert(lista,0,n)
    lista_ordenada= list.sort(numero_inserido)
    return lista_ordenada