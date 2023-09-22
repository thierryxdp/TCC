def freq_palavras(frases):
    i = 0
    lista = frases.split()
    dic = {}
    c = 0
    for j in range(len(lista)):
        for a in range(len(lista)):
            if lista[i] == lista[a]:
                c = c + 1
        dic[lista[i]] = c
        i = i + 1
    return dic