def freq_palavras(frases):
    """
    	Retorna um dicionário que diz quantas vezes cada palavra aparece na frase informada
    	str -> dict
    """
    substrings=frases.split()
    dicio={}
    for i in range(len(substrings)):
        dicio[substrings[i]] = substrings.count(substrings[i])
    return dicio