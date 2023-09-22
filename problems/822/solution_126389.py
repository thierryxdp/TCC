def repetidos(lista):
	resposta = 0  
    
    while contador<len(lista):
        if lista[contador]==lista[contador-1]:
            resposta+=1
            contador +=1
    return resposta