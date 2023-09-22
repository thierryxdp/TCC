def filtra_pares(tupla):
    """ - """

    contador = 0
    resposta = []
    
    while contador < len(tupla):
        if tupla[contador]%2 == 0:
            resposta.append(tupla[contador])
        contador = contador + 1
    return tuple(resposta)