def insere (lista_numero,n):
    lista_numero.sort()
    lista_numero=list() 
    for c in lista_numero:
        if c < n:
            lista_numero.append(c)
    return lista_numero