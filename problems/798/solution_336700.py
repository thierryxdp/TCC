def freq_palavras(frases):
    ''' retorna um dicionário que relaciona strings 
    com o número de vezes que elas aparecem, one as strings são as chaves;
    str->dict'''
    dicionario={}
    frases=frases.strip()
    frases=frases.split('')
    for palavra in frases:
        if palavra not in dicionario:
            dicionario[palavra]+=1
        else:
            dicionario[palavra]=1
    return dicionario