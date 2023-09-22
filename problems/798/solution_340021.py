def freq_palavras(frase):
    i=0

    while i<len(frase):
        palavras=(str.split(frase))
        ocorrencias=list.count(,palavras,palavras[i])
        dicionario={palavras[i]:ocorrencias}
        i=i+1
    return dicionario