def freq_palavras(texto):
    d={}
    texto=str.split(texto)
    for x in texto:
        if texto[x] == texto[x+1]:
            d=d+{texto[x]}+ {x+1}