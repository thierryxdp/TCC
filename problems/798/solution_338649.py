def freq_palavras(frases):
    '''recebe uma string e retorna um dicionário onde cada palavra dessa
    string seja uma chave e tenha como valor o número de vezes que a
    palavra aparece'''
    d={}
    for x in frases:
        d=d + {"frases[x]":str.find(frases[x])
    return d