def freq_palavras(frases):
    '''Função que recebe uma frase na forma de string e
    retorna um dicionario com o numero de vezes que a
    palavra dessa string aparece.
    str -> dict
    '''
    dicio = {}
    palavra = frases.split()

    for elementos in palavra:
        dicio[palavra[i]] = palavra.count(palavra[i])

    return dicio