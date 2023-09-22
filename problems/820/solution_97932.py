def posLetra(frase, letra, n):
    """função que recebe uma frase, uma letra e um número
    inteiro n, que indica a ocorrência desejada da letra,
    e retorna em que posição a ocorrência desejada da letra
    se encontra.
    str, str, int -> int"""

    i = 0
    posicoes = []

    while i < len(frase):
        if frase[i] == letra:
            posicoes += [i]
        i += 1

    if n > len(posicoes):
                return -1

    return posicoes[n-1]