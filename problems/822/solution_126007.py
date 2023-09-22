def repetidos (lista):
    '''dada um lista retorna o numero de vezes que um elemtno da lista é igual ao anterior'''
    '''list -> int'''
    
    i=0
    rep = 0
  
    
	while i < (len(lista)-1):
		if lista[i] == lista[i+1]:
			rep = rep + 1
            
        
		i = i + 1
        
	return rep