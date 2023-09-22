def posLetra(frase, letra, n):
    '''Encontra a posição da n-ésima ocorrência da letra dada na frase dada
    str, str, int --> int'''
    i = 1
    contador = 0
    while i < len(frase):
        if letra == frase[i]:
            contador += 1
        if contador == n:
            return i
        i += 1
    # caso o while rode a lista toda sem retornar, o número de ocorrências é menor que n
    return 1