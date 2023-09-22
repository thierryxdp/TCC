def posLetra(frase, letra, x):
    '''Entre com uma frase, uma letra e um numero para ser retornado a posição
    que da ocorrencia desejada de acordo com o numero dado
    String, Char, Int -> Int'''
    i=0
    cont=()
    
    while i<len(frase):
        
        if letra==frase[i]:
            y=i
            cont=cont+(i, )
            
    	i=i+1
           
    if len(cont)<x:
        return -1
    
    if len(cont)>x:
        return cont
    
	else:  
    	return cont[-1]