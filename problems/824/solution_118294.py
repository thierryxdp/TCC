def uppCons(frase):
    '''retorna a frase com as consoantes em maiúscula
    	str -> str'''
    
    i=0
    frase_final=''
    
    while i<len(frase):
        
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
        	consoante=frase[i].upper()
        
    		frase_final=frase_final + consoante
            
        else:
            frase_final=frase_final + frase[i]
        
    	i=i+1
        
    return frase_final