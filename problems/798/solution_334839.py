def freq_palavras(frases):
    lista = str.split(frases)
    for n in lista:
        qtd = list.count(lista, n)
        dic = {n: qtd}
    return dic