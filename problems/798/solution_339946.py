freq_palavras(frases):
    dic = {}
    lista = []
    palavra = ''
    for i in frases:
        if i != '' and i != '.' and i != '?' and i != ',':
            palavra += i
        else:
            if palavra != '':
                list.append(lista,palavra)
                palavra = ''
    if palavra != '':
        list.append(lista,palavra)
                palavra = ''
    for p in lista:
        dic[p] = list.count(lista,p)
    return dic