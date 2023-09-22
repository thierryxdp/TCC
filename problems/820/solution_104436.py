def posLetra(frase, letra, num):
    '''função que recebe uma string, uma letra e um número'''
    posicao = frase.find(letra)
    while posicao >= 0 and num > 1:
        posicao = frase.find(letra, posicao + 1)
        num -= 1
    return posicao