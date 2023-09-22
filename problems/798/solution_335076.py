def freq_palavras(frases):
    dicio = {}
    n = 1
    frasedit = str.split(frases,' ')
    for palavra in frasedit: ## pra cada palavra na lista
        	if palavra in dicio: ###se ela tiver na frase
            	dicio[palavra] = n ### atribui n
                n[palavra]+=1 ### n aumenta
            elif palavra in frases:
                dicio[palavra] = n
                
    return dicio