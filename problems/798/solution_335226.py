def freq_palavras(frases):
    '''Função que recebe uma frase e retorna um dicionário com o numeros 
    de vezes que cada palavra aparece
    str -> dict
    '''
    dicio={ }
    frases=frases.split()
    for i in range(len(frases)):
        dicio[frases[i]] = frases.count(frases[i])
    return dicio