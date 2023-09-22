def insere(lista_numero,n):
    b = [n]
    if n in lista_numero:
        return sorted(lista_numero)
    elif n not in lista_numero:
        lista = lista_numero + b
        return sorted(lista)