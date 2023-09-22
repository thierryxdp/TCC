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
            dic[p] = list.count(lista,p)
    del dic['']       
    return dic