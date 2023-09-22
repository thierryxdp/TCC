def freq_palavras (frases):
    """Função que recebe um string e ira retornar um dicionario
    onde as palavras são chaves e o valor será o número de vezes
    que a palavra aparece. str -> dict"""
    palavras = " "
    i = 0
    for palavras in frases:
        if palavras[i]:
            frases = list.count(frases, palavras[i])
            palavras = dict(frases)
    return palavras