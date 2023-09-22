def freq_palavras(frases):
    num_palavra = frases.split()
    dicionario = {}
    i = 0 
    for numero in num_palavra:
        dicionario[num_palavra[i]] = num_palavra.count(num_palavra[i])
        i = i + 1
    return dicionario