def posLetra(frase, letra, num):
    '''Função que recebe uma string, uma letra e um número
    e retorna em que posição da string aquela ocorrência está
    str, str, int -> int'''
    
    posicao = frase.find(letra)
    
    while posicao >= 0 and num > 1:
        posicao = frase.find(letra, posicao +1)
        num += 1
    return posicao