def insere (lista_numero, n):
    a = str(lista_numero)
    b = a.replace('[','').replace(']','')
    c = b.split(',')
    return c