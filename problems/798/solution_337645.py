def freq_palavras(frases):
    '''
    Função que recebe uma frase e retorna um dicionário com as palavras 
    da frase como chaves e os valores sendo o numero de ocorrência da 
    palavra na frase.
    str -> dict
    '''
    frases = frases.split()
    dicio = dict()
    for i in range(len(frases)):
        if frases[i]not in dicio:
           dicio[frases[i]] = 1
        else:
            dicio[frases[i]] += 1
    return dicio