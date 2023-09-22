def uppCons(frase):
    '''retorna a frase com as consoantes em maiúscula
    	str -> str'''
    
    i=0
    
    if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
        frase[i].upper()
        
    i=i+1
        
    return frase