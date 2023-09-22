def freq_palavras(frases):
    ''' retorna uma lista contendo a quantidade de vezes que as palavras
    aparecem em uma frase.
    str -> list'''

    palavras1 = str.split(frases.lower())
    palavras2 = str.split(frases.lower())
    ocorrencias = []
    contada = []
    for palavra1 in palavras1:
        contagem = 0
        for palavra2 in palavras2:
            if (palavra1 == palavra2):
                contagem = contagem + 1
        list.append(contada, palavra1)
        repetida = -1
        for palavras in contada:  
            if (palavras == palavra1):
                repetida = repetida + 1
        if (repetida < 1):
            list.append(ocorrencias, str(palavra1)+': '+str(contagem))
        
    return ocorrencias