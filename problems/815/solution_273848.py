def insere(lista_numero,n):
    if n not in lista_numero:
        lista_numero.append(n)
    lista_numero.sort()
    return lista_numero