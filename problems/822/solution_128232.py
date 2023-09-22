def repetidos(lista):
    nova_lista = []
    for numero in lista:
        if numero in nova_lista:
            nova_lista.append(numero)
    return len(nova_lista)