def posLetra(fra,pala,pos):
    quant=0
    i=0
    quant_rep=fra.count(pala)
    if pos<=quant_rep:
    	while i<len(fra):
        	if fra[i] in pala:
                quant=quant+fra[i].count(pala)
                if quant>=pos:
                    
        	i=i+1
            
    else:
        return -1