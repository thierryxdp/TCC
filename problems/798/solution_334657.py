def freq_palavras(frases):
    palavras=frases.split()
    quant_palavra={}
    for palavra in palavras:
        if palavra in quant_palavra:
            quant_palavra[palavra]+=1
        else:
            quant_palavra[palavra]=1
  	return quant_palavra