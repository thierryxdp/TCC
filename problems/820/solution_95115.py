def posLetra(frase,letra,num):
    '''Escreva uma frase e uma letra. A funcao conta quantas vezes
    a letra dada aparece na frase. Caso seja maior ou igual
    que o numero dado, retorna em que posicao a letra se encontra;
    caso seja menor, retorna -1. Considere a primeira letra da frase
    como posicao 0, segunda letra posicao 1, e assim sucessivamente.
    str, str, int -> int'''
    i=0
    contador=0
    while i<len(frase):
        if letra in frase[i]:
            contador=contador+1
        i=i+1
    if contador>=letra:
        return frase.find(letra)
    else:
        return -1