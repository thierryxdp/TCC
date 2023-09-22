def repetidos(listNum):
    
    resposta = 0
    num1 = 0
    nList = (len(listNum) - 1)
    
    while num1 < nList:
        
        if num1 < len(listNum):
            if listNum[num1] == listNum[num1+1]:
        		resposta += 1
        
        	else:
            	pass
        
        	num1 += 1
        
        else:
            pass
        
	return resposta