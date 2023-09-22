def freq_palavras(frases):
    '''Recebe uma string e retorna um dicionario onde cada
    palavra dessa string é uma chave e tem como valor
    o numero de vezes que a palavra aparece'''
    palavras=frases.split()
    dicionario={}
    for palavra in palavras:
        if palavra in dicionario:
            dicionario[palavra]+=1
        else:
            dicionario[palavra]=1
    return dicionario