def freq_palavras(frases):
    '''retorna a frequencia que as palavras da frase aparecem;
    str->dict'''
    dici={}
    a=str.split(frases)
    for palavra in a:
        dici[palavra]=str.count (frases,palavra)
    return dici