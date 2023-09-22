def posLetra(frase:str, letra:str, n:str)->int:
    '''Encontra a posição da n-ésima ocorrência da letra dada na frase dada'''
    i = 0
    contador = 0
    while i < len(frase):
        if letra == frase[i]:
            contador += 1
        if contador == n:
            return i
        i += 1
    # caso o while rode a lista toda sem retornar, o número de ocorrências é menor que n
    return -1