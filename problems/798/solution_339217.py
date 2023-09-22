def contador (iteravel, elem):
    '''Conta quantas vezes um elemento aparece no iterável
str/lista/tupla, str-> int'''
    iteravel=str(iteravel)
    #Transformação necessária para quando os elementos de uma tupla/lista não são strings, mas inteiros, então o contador não conseguia processá-los.
    quantidade = 0
    for elemento in range(len(iteravel)):
        if elem in iteravel[elemento]:
            quantidade = quantidade + 1
    return quantidade

def freq_palavras (frases):
    '''Constroi um dicionário com a quantidade de vezes que cada palavra aparece na frase
    str -> dict'''
    for elemento in range(len(frases)):
        quantidade = contador (frases, frases[elemento])
        return {frases[elemento]:quantidade}