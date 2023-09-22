def freq_palavras(frases):
    dicionario={}
    frases1=str.split(frases,)
    for frase in frases1 :
       
        dicionario[frase]=list.count(frases1,frase)
    return dicionario