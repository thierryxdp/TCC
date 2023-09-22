def repetidos(lista):
    nova_lista = []
    repetidos = []
    for numero in lista:
        if numero in nova_lista:
            repetidos.append(numero)
        else:
            nova_lista.append(numero)
    return len(repetidos)