def freq_palavras(frases):
    '''A função recebe uma frase e
    retorna um dicionário com a quan-
    tidade de palavras da frase.
    str --> dict'''

    palavras = str.split(frases)
    list_freq = {}
    counter = 0
    limit = len(palavras)

    while counter < limit:
        list_freq[palavras[counter]] = palavras.count(palavras[counter])
        counter += 1

    return list_freq