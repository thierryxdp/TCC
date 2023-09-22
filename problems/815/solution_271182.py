def insere(lista_numero,n):
    numero_inserido_lista= list.insert(lista_numero,len(lista_numero),n)
    lista_ordenada= list.sort(numero_inserido_lista)
    return lista_ordenada