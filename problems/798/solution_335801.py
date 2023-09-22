def freq_palavras(frases):
    """
	Retorna quantas vezes a palavra apareceu na frase.
    str -> dict
    """
    palavras= str.lower(frases)
    palavras= str.split(frases)
    palavras.sort()
    dicio={}
    repeticao=1
    for i in range(0,len(frases)-1):
        if palavras[i] == palavras[i+1]:
            repeticao+=1
            dicio[palavras[i]]= repeticao
        else:
            repeticao= 1
            dicio[palavras[i]]= repeticao
    return dicio