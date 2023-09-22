def freq_palavras(frases):
    '''Recebe uma string e retorna um dicionario onde cada
    cada palavra dessa string seja uma chave e tenha como
    valor o numero de vezes que a palavra aparece'''
    i=0
    str.split(frases,' ')
    dicio={}
    for x in frases:
        dicio = {x:(list.count(frases,x))}
    return dicio