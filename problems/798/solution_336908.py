def freq_palavras(frases):
    '''Dado uma strig, retorna um dicionário em que cada palavra dessa string
seja uma chave com o número de vezes qe a palavra aparece. string--> decionário.
    '''
    dicionario = {}
    frases = frases.split()
    for i in range(len(frases)):
        dicionario[frases[i]] = frases.count(frases[i])
    return dicionario