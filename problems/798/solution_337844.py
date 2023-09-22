def freq_palavras(frases):
    '''Função que receba uma string e retorne uma palavra dessa string seja chave e tenha o número de vezes que aparece, str -> dicionário'''
    oracao = str.split(frases, ' ')
    palavras = {}
    for x in oracao:
        if x in palavras:
            palavras[x] += 1
        if x not in palavras:
            palavras[x] = 1
    return palavras