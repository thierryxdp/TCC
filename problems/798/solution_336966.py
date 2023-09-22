def freq_palavras(frases):
    '''str -> dict '''
    y=str.split(frases)
    x={}
    for palavra in y:
        x[palavra]=list.count(y,palavra)
    return x