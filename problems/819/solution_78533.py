def filtraMultiplos(lista,numero):
    """..."""
    nova_lista = list()
    num_lista = len(lista)
    i = 0
    while (i <= num_lista):
        divisao = lista[i]/numero
        resto = lista[i]%numero
        if resto == 0:
        i += 1
    return resto