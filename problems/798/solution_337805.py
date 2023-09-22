def freq_palavras(frases):
    '''Função que receba uma string e retorne uma palavra dessa string seja chave e tenha o número de vezes que aparece, str -> dicionário'''
    palavras = dict()
    oracao = str.split(frases, '') 
    for x in oracao:
        if x not in palavras:
            palavras[x] == 1
        for x in oracao:
            if x in oracao:
                palavras[x] = palavras + 1
    return palavras