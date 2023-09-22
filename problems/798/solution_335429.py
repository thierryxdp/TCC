def freq_palavras(frase):
    ''' funcao recebe uma frase e retorna um dicionario informando
    quantas vezes cada palavra foi usado nessa frase. str-->dic'''
    d={}
    for c in frase:
        if c in not d:
            d[c]= 1
        else:
            d[c]+= 1
    return d