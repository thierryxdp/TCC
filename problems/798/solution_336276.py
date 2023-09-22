def freq_palavras(frases):
    ''' Recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave
    e tenha como valor o número de vezes que a palavra aparece.
    str->dict
    '''
    dicio={}
    frases=frases.split()
    for x in range(len(frases)):
        if frases[x] not in dicio:
            dicio[frases[x]]=1
        else:
            dicio[frases[x]]+=1
    return dicio