def freq_palavras(frases):
    '''Função que retorna um dicionário com cada palavra presente 
    na string frases e o numero de vezes que a palavra aparece.
    str -> dict'''
    dicionario= {}
    frases= frases.split()
    for palavra in frases:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionari