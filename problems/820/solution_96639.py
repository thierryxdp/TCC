def posLetra(frase,letra,n):
    '''Dado uma frase, uma letra e um numero n que indica a ocorrencia desejada da letra,
    a funcao retorna que posicao da frase a ocorrencia esta.
    str, str, int'''
    numletra=0
    i=0
    while n>numletra:
        if frase[i]==letra:
            numletra=numletra+1
    	i=i+1
    return i+1