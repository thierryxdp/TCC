def insere(lista_numero,n):
    type(lista_numero) == list and type(n)== int
    lista_numero.append(n)
    nova_lista =sorted(lista_numero)
    return nova_lista