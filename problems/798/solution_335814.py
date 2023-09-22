def freq_palavras(frases):
    '''
    retorna em dicionario, a quantidade de vezes que cada palavra aparece na frase
    str -> dict
    '''
    recorrencia={}
    frases=frases.split()
    for identificador in range(len(frases)):
        frases.count(frases[identificador])
        recorrencia[frases[identificador]]= frases.count(frases[identificador])
    return recorrencia