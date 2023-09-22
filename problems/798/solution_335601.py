def freq_palavras(frases):
    '''retorna a frequencia que as palavras da frase aparecem;
    str->dict'''
    dici={}
    a=str.split(frases)
    for palavra in a:
        if len(palavra)==1 and not palavra in 'AEIOU':
            dici[palavra]=str.count(frases,' '+palavra+' ')
        else:
            dici[palavra]=str.count (frases,palavra)
    return dici