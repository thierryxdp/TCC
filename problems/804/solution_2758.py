def filtra_pares(tupla=[x1]): 
    
    elemPares = ''
    
    if tupla[:1] % 2 == 0:
        elemPares = tupla[:1]
    
    elif tupla[1:2] % 2 == 0:
        elemPares = tupla[1:2]
        
    elif tupla[2:3] % 2 == 0:
        elemPares = tupla[2:3]
        
    elif tupla[3:4] % 2 == 0:
        elemPares = tupla[3:4]
        
	return elemPares