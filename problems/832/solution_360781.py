def eh_quadrada(matriz):
	quant_ele=[]
    acumu=0
    if len(matriz)>1:
   		for i in matriz:
    		list.append(quant_ele,len(i))
    		for j in range(len(matriz)):
    			if quant_ele[0]!=quant_ele[j]:
            		acumu=acumu+1
		if acumu<=0:
        	return True
		else:
    		return False
    else:
        return False