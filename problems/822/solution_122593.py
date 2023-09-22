def repetidos(numeros):
    """Funcao que recebe uma lista de numeros: numeros e retorna o numero de
    vezes que um elemento da lista e igual ao elemento anterior """

    contador = 1
    num_repetidos = 0

    while contador < len(numeros):
        if numeros[contador] == numeros[contador-1]:
            num_repetidos += 1
        contador += 1

    return num_repetidos