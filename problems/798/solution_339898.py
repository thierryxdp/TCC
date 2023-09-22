def freq_palavras(frases):
    palavras = str.split(frases)
    ocorrencias = { }
    
    for palavra in palavras:
        if palavra in ocorrencias:
            ocorrencias[palavra] +=1
        else:
            ocorrencias[palavra] = 1
        return ocorrencias