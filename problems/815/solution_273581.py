def insere(lista_numero,n):
    type(lista_numero) == list and type(n)== int
    nova_lista = lista_numero.append(n)
    sorted(nova_lista)
    return nova_lista