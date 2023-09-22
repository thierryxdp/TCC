def freq_palavras(frases):
    fraseLista=frases.split(' ')
    dic={}
    
    for i in range(len(fraseLista)):
        if fraseLista[i] in fraseLista:
        	n=fraseLista.count(fraseLista[i])
        	dic={fraseLista[i]:n}
    return dic