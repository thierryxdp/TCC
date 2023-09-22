def posLetra(frase,letra,n):
    '''Dado uma frase, uma letra e um numero n que indica a ocorrencia desejada da letra,
    a funcao retorna que posicao da frase a ocorrencia esta.
    str, str, int'''
    i=0
    vogal=''
    while i<len(frase):
        if frase[i]==letra:
            vogal=frase.find(letra)
            i=i+1
    return vogal