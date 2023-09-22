def freq_palavras(frases):
    '''retorna a frequencia que as palavras da frase aparecem;
    str->dict'''
    dici={}
    a=str.split(frases)
    for palavra in a:
        dici[palavra]=0
    for palavra in a:
        dici[palavra]=dict.get(dici,palavra)+1
    return dici