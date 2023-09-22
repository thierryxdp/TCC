def freq_palavras(frases):
    lista = str.split(frases)
	dic = {}
    for n in lista:
        qtd = list.count(lista, n)
        if n not in dic:
            dic[n] = qtd
    return dic