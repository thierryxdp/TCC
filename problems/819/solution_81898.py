def filtraMultiplos(lista, numero):
    ''' Função que filtra os múltiplos de um número contido em uma lista e adiciona estes números em uma nova lista.
    ist,int -> list'''
    i = 0
    resultado = []
    while i < len(lista):
        if lista[i] % numero == 0:
            resultado.append(lista[i])

        i = i + 1

    return resultado