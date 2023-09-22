def freq_palavras(frases):
    '''Função que dada uma string (frases), retorna um dicionário 
    com cada palavra presente na string e sua frequência relativa
    str -> dict '''
    D = {}
    frases = frases.split()
    for i in frases:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
    return D