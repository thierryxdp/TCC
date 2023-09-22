def posLetra(frase, letra, ocorrencia):
    '''Função que retorna em que posição da string aquela
    ocorrência da letra está ao receber como entrada uma
    string, uma letra e um número que indica a ocorrência
    desejada.'''
    #caso exista menos ocorrências da letra do que a ocorrência pedida,
    #a função retorna -1.
    #str, str, int -> int
    i = 0
    nocs = 0
    while i < len(frase) and nocs < ocorrencia:
        if frase[i] == letra:
            nocs = nocs +1
        i = i + 1
    else:
        return i -1