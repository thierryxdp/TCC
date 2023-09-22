def freq_palavras(frases):
    lista = str.split(frases)
    d = {}
    for i in lista:
        d[i] = list.count(lista,i)
        
    return d