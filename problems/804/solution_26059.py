filtra_pares(tupla):
    """ - """

    contador = 0
    reposta = []
    
    while contador < len(tupla):
        if tupla[contador]%2 == 0:
            reposta.append(tupla[contador])
        contador = contador + 1
    return tuple(reposta)