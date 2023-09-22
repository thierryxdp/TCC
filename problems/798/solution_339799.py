def freq_palavras(frases):
    ''' retorna uma lista contendo a quantidade de vezes que as palavras
    aparecem em uma frase.
    str -> list'''

    palavras1 = str.split(frases)
    palavras2 = str.split(frases)
    ocorrencias = {}
    for palavra1 in palavras1:
        contagem = 0
        for palavra2 in palavras2:
            if (palavra1 == palavra2):
                contagem = contagem + 1
            ocorrencias[palavra1] = contagem     
    return ocorrencias