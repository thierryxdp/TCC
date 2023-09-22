def freq_palavras(frases):
    dicionario=[]
    palavras=frases.split()
    
    for coisa in palavras:
        if palavras.count(coisa)>0:
            soma=list.append(dicionario,coisa)
            dicionario=list.append(soma,palavras.count(coisa))
        return dicionario