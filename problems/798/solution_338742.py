def freq_palavras(frases):
    lista1 = []
    n = 0
    frases1 = str.split(frases,' ')
    for i in range(len(frases1)):         
        if frases1[i] not in lista1:
            lista1 += [frases1[i],]
    return lista1