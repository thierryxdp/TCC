def freq_palavras(frases):
    str->dict
    dicionario
   	for linha in frase:
        linha=linha.strip()
        linha=linha.lower()
        palavras=linha.split(" ")
        
  	for palavra in palavras:
        if palavra in dicionario:
            d[palavra] = d[palavra] + 1
       	else:
            d[word] = 1
  	for qnt in list(d.keys()):
        return(qnt,":"d[qnt])