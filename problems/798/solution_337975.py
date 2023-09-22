def freq_palavras(frases):
    '''
    função que recebe uma string e retorna um dicionário onde cada palavra dessa
    string é uma chave e tem como valor o numero de vezes que a palavra aparece.
    str->dict
    '''
    dicionario = {}
    y=str.split(frases)
    
    for x in y:
        if x in y:
            dicionario[x]=list.count(y,x)
    return dicionario