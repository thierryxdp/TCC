def freq_palavras(frases):
    dic = {}
    lista = []
    palavra = ''
    sinais = (',','.',' ','?')
	for i in frases:
        if i not in sinais:
            palavra += i
        else:
            if palavra != '':
                list.append(lista,palavra)
                palavra = ''
    if palavra != '':
        list.append(lista,palavra)
    for p in lista:
        dic[p] = list.count(lista,p)
    return dic