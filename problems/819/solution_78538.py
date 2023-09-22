def filtraMultiplos(lista,numero):
    """..."""
    reposta = list()
    num_lista = len(lista)
    i = 0
    while (i <= num_lista):
        divisao = lista[i]/numero
        resto = lista[i]%numero
        if reposta(resto):
    		i += 1
    return resposta