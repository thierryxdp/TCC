def freq_palavras(frases):
    fraseLista=frases.split(',')
    fraseLista=''.join(fraseLista)
    fraseLista=fraseLista.split(' ')
    dic={}
    for i in fraseLista:
        n=fraseLista.count(fraseLista[i])
        dic={fraseLista[i]:n}
    return dic