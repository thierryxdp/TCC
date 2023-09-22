def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário cujas
chaves são cada palavra da frase e os valores são o número
de vezes que a palavra existe na frase.
str -> dict
"""
    d = {}
    palavras = str.split(frases)
    for i in palavras:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d