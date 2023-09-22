def freq_palavras(frases):
    palavra = ''
    lista = []
    dic = {}
    for termo in frases:
        if termo not in ' .,;!?':
            palavra = palavra + termo
        else:
            lista = lista + [palavra]
            palavra = ''
    
    for p in lista:
        if ' .,;!?' not in p:
            dic[p] = list.count(lista,p)