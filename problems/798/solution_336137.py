def freq_palavras(frases):
    contagem = {}
    lista = str.split(frases)
    for palavras in lista:
        quantidade = list.count(lista,palavraz)
        contagem[palavras] = quantidade
    return contagem