def freq_palavras(frases):
    """"""
    soma = 0
    lista = str.split(frases)
    for c in lista:
        soma += c
    return soma