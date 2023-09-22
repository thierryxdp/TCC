def insere(lista_numero, n):
    a = lista_numero
    a[0:0] = [n]
    b = sorted(a)
    return b