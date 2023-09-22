def freq_palavras(frases):
    lista = str.split(frases)
    for n in lista:
        qtd = list.index(lista, n)
        dic = {n: qtd}
    return dic