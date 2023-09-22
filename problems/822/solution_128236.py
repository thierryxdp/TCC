def repetidos(lista):
    nova_lista = []
    repetidos = []
    rep = []
    for numero in lista:
        if numero in nova_lista:
            repetidos.append(numero)
            if numero in repetidos:
                rep.append(numero)
        else:
            nova_lista.append(numero)
    return len(rep)