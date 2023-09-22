def insere(lista_numero,n):
    numero_inserido= lista_numero[len(lista_numero):len(lista_numero)]= [n]
    lista_ordenada= list.sort(numero_inserido)
    return numero_inserido