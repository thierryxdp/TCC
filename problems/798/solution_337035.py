def freq_palavras(frases):
    '''Calcula a frequência de cada palavra em uma string
    retornando um dicionário com as palavras e suas respectivas frequências
    str --> dict'''

    freq_por_palavra = {}
    frases = frases.split()

    for i in frases:
        if i in freq_por_palavra:
            freq_por_palavra[i] += 1
        else:
            freq_por_palavra[i] = 1
    return freq_por_palavra