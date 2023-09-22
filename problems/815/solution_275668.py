def insere(lista_numero,n):
    lista_numero.extend(n) 
    sorted(lista_numero, key=int)
    return lista_numero