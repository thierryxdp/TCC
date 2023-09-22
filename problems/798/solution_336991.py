def freq_palavras(frases):
    palavras=frases.split()
    contagem={}
    for i in palavras:
        n=list.count(palavras,i)
        contagem={contagem+i:n}
    return contagem