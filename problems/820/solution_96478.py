def posLetra(frase,letra,n):
    '''Dado uma frase, uma letra e um numero n que indica a ocorrencia desejada da letra,
    a funcao retorna que posicao da frase a ocorrencia esta.
    str, str, int'''
    i=0
    posicao=0
    while i<len(frase):
        if letra in frase:
            posicao=str.find(frase,letra)
            posicao=str.find(frase,letra,1)
            return posicao
        else:
            return -1