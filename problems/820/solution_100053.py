def posLetra(fra,pala,pos):
    quant=[]
    i=0
    quant_rep=fra.count(pala)
    if pos<=quant_rep:
    	while i<len(fra):
        	if fra[i] in pala:
                list.append(quant,i)
                print(quant)
                print(i)
        	i=i+1
        return quant[pos-1]    
    else:
        return -1