def repetidos(listNum):
    
    resposta = 0
    num1 = 0
    
    while num1 < len(listNum):
        if listNum[num1] == listNum[num1+1] and num1 <= len(listNum):
        	resposta += 1
        
        else:
            pass
        
        num1 += 1
        
	return resposta