def freq_palavras(frase):
    palavras=str.split(frase)
    i=0

    while i<len(palavras):
        
        ocorrencias=palavras.count(palavras[i])
        dicionario={palavras[i]:ocorrencias}
        i=i+1
    return dicionario