def freq_palavras(frases):
    """retorna um dicionario cuja a chave é uma palavra presente em
    'frases' e tem como valor sua quantidade de aparições;
    str->dict{str:int}"""
    dicio={}
    for palavra in str.split(frases,' '):
        if palavra in dicio:
            dicio[palavra]+=1
        if palavra not in dicio:
            dicio[palavra]=1
    return dicio