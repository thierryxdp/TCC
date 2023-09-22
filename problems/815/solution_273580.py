def insere(lista_numero,n):
    type(lista_numero) == list and type(n)== int
    nova_lista = lista_numero.append(n)
    nova_lista.sort()
    return nova_lista