def freq_palavras(frases):
    'recebe uma str e retorna um dicionario com o numero de vezes que as palavras aparecem'
    frases=frases.split()
    dicionario={}
    for palavra in frases:
        dicionario[palavra]=0
    for palavra in frases:
        dicionario[palavra]+=1
    return dicionario