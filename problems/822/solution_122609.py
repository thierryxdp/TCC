def repetidos(listNum):
    
    resposta = 0
    num1 = 0
    
    while num1 < len(listNum):
        
        if num1 < (len(listNum) - 1):
            if listNum[num1] == listNum[num1+1]:
        		resposta += 1
        
        	else:
            	pass
        
        	num1 += 1
        
        else:
            pass
        
	return resposta