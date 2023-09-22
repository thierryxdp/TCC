def posLetra(frase,letra,n):
    '''Dado uma frase, uma letra e um numero n que indica a ocorrencia desejada da letra,
    a funcao retorna que posicao da frase a ocorrencia esta.
    str, str, int'''
    posicao=0
    i=0
    while i<len(frase):
        if letra in frase:
            posicao=str.find(frase,letra)
        if n=1:
            return posicao
        if n=2:posicao=str.find(frase,letra,posicao)
            return posicao