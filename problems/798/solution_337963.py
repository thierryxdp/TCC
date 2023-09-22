def freq_palavras(frases):
    '''
    função que recebe uma string e retorna um dicionário onde cada palavra dessa
    string seja uma chave e tenha como valor o numero de vezes q a palavra acontece.
    str->dict
    '''
    dicionario = {}
    y=str.split(frases)
    
    for x in y:
        if x in y:
            dicionario[x]=list.count(y,x)
    return dicionario