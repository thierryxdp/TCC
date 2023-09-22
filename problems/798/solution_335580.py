def freq_palavras(frases):
    '''retorna a frequencia que as palavras da frase aparecem;
    str->dict'''
    dici={}
    a=str.split(frases)
    for palavra in frases:
        dici=[palavra]=str.count (frases,a[0],palavra)
    return dici