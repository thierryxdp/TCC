def posLetra(texto,letra,ocorrencia):
    '''Funcao que recebe uma string, uma letra e um numero. O numero indica a
        ocorrencia desejada da letra (1 para primeira ocorrencia,
        2 para segunda, etc). A funcao deve retornar em que posicao da string
        aquela ocorrencia da letra estao. Caso exista menos ocorrencias
        da letra do que a ocorrencia pedida, a funcao deve retornar -1.'''
    i = 0
    n = 0
    while i<len(texto) and n<ocorrencia:
        if texto[i] == letra:
            n = n +1
        i = i + 1
    if n < ocorrencia:
        return -1
    else:
        return i-1