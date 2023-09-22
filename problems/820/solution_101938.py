def posLetra(frase, x, n):
    palavras = ''    
    i=0
    if x in frase[n]:
        palavras = str.index(frase, x, n)
    else:
        palavras = -1
    i=i+1
    return palavras