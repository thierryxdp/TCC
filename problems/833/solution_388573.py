def conta_numero(numero,matriz):
    '''''''
    contador = 0
    for linha in matriz:
        for coluna in linha:
            if numero == coluna:
                contador += 1
    return contador