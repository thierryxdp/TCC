def freq_palavras(frases):
    dicionario={}
    contador=0
    a=str.split(frases)
    while contador<len(str.split(frases)):
        dicionario[a[contador]]=list.count(a,a[contador])
        contador=contador+1
    return dicionario