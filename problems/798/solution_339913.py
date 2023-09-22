def freq_palavras(frases):
    #retorna dicionário com a quantidades de vezes que cada palavra aparece
    dic = {}
    lista = []
    palavra = ''
    indice = 0
    for i in frases:
        if i != ' ' and i != '.' and i != ',':
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