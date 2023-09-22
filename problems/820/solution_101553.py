def posLetra(fra,pala,pos):
    '''Recebe uma frase,fra, uma palavra,pala,
    e um número,pos, e retorna a posição em que
    a pala que repetiu em pos vezes em fra
    str,str,int->int'''
    quant=[]
    i=0
    quant_rep=fra.count(pala)
    if pos<=quant_rep:
    	while i<len(fra):
        	if fra[i] in pala:
                list.append(quant,i)
        	i=i+1
        return quant[pos-1]    
    else:
        return -1