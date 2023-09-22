def posLetra(frase,letra,ocorrencia):
    '''funcao que retorna a posição em que a ocorrencia de dada letra pertencente a uma certa string está
    str-->int'''
    proximo = 0
    posicao = ['']
    while proximo < len(frase):
        if letra in frase:
            posicao = frase[letra][ocorrencia]
    proximo=proximo+1
    return posicao