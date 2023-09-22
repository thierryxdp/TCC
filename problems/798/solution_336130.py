def freq_palavras(frases):
    contagem = {}
    lista = str.split(frases)
    for palavras in lista:
        quantidade = list.count(str.split(frases))
        contagem[palavras] = quantidade
    return contagem