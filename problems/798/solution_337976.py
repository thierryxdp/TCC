def freq_palavras(frases):
    '''
    str->dict
    '''
    lista = {}
    y=str.split(frases)
    
    for x in y:
        if x in y:
            lista[x]=list.count(y,x)
    return lista