def freq_palavras(frases):
    '''Função que dada um string, retorna um dicionário onde cada palavra dessa string é uma chave e tem valor o número de vezes que a palavra aparece
       str->dicionário'''
    dicionario={}
    f=str.split(frases)
    i=0
    while i<len(f):
        lista=list.count(f,f[i])
        dicionario[f[i]]=lista
        i=i+1
    return dicionario