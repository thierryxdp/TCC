def freq_palavras(frases):
    fraseLista=frase.split(',')
    fraseLista=''.join(fraseLista)
    fraseLista=fraseLista.split(' ')
    dic={}
    for i in fraseLista:
        n=list.count(fraseLista,fraseLista[i])
        dic={fraseLista[i]:n}
    return dic