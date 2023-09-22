def freq_palavras(frases):
    contagem = {}
    lista = str.split(frases)
    for palavras in lista:
        quantidade = list.count(lista,0)
        contagem[palavras] = quantidade
    return contagem