def freq_palavras(frases):
    'retorna um dict com os indices e as palavras da frase e sua frequencia'
    'str----dict'
    dicionario={}
    palavras=frases.split(' ')
    for palavra in palavras:
        if palavra in list(dicionario.keys()):
            dicionario[palavra]+=1
        else:
            dicionario[palavra]=1
    return diciona