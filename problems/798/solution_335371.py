def freq_palavras(frase):
    dicionario={}
    contador=0
    a=str.split(frase)
    while contador <len(str.split(frase)):
        dicionario[a[contador]]=list.count(a,a[contador])
        contador= contador +1
    return dicionario