def inverte (frase):
    
    msg = list.reverse(frase)
    
#primeiro retirar a pontuação:
    
    if '-' in frase:
        msg = str.replace(frase,'-',' ') 
    
    if ',' in frase:
        msg = str.replace(frase,',',' ') 
    
    if ':' in frase:
        msg = str.replace(frase,':',' ') 
    
    if ';' in frase:
        msg = str.replace(frase,';',' ') 
    
    elif '.' in frase:
        frase = str.replace(frase,'.',' ') 
        
    elif '!' in frase:
        msg = str.replace(frase,'!',' ') 
        
    elif '?' in frase:
        msg = str.replace(frase,'?',' ') 
    
    elif frase == FRASE:
        msg = str.lower(frase)
        
    
               
    return frase