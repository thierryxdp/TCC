def freq_palavras(frases):
    dicionario={}
    frases1=str.split(frases)
    for frase in frases1 :
       
        dicionario[frase]=str.count(frases,frase)
    return dicionario