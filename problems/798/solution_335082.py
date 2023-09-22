def freq_palavras(frases):
    dicio = {}
    n = 1
    frasedit = str.split(frases,' ')
    for palavra in frasedit: ## pra cada palavra na lista
        	if palavra in dicio: ###se ela tiver no dicionario
            	dicio[palavra] = dicio[palavra]+1 ### atribui n
            elif palavra not in dicio:
                dicio[palavra] = n
                
    return dicio