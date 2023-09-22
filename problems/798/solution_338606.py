def freq_palavras(frase):
    l=list(str.split(frase," "))
    g=int
    for y in l:
        g=str.count(y,frase)
    return dict(y=g)