def posLetra(palavra,letra,ocorrencia):
    '''funcao que retorna a posição em que a ocorrencia de dada letra pertencente a uma certa string está
    str-->int'''
    posicao=palavra.find(letra)
    while posicao>=0 and ocorrencia>1:
        if letra != palavra:
            return -1
        posicao= palavra.find(letra,posicao+1)
        proximo=proximo-1
    return posicao