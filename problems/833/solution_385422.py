def conta_numero(numero, matriz):
    """ Verifica se na matriz existe um determinadonúmero 
    e se existir conta quantas vezes ele se repete nesta lista.
    list-> int"""
    contador = 0
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if matriz[lin][col] == numero:
                contador += 1
    return contador