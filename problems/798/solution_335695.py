def freq_palavras(frases):
    '''retorna um dicionario onde cada palavra é associada ao numero de vezes que ela aparece na frase; srt -> dict'''
    n=str.split(frases," ")
    b={}
    for x in n:
        a=str.count(frases,x)
        b[x]=a
    b[list(dict.keys(b))[len(list(dict.keys(b)))-1]]=1
    return b