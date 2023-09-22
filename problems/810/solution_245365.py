def inverte (frase):
    
    #primeiro retirar a pontuação:
    
    if '-' in frase:
        frase = str.replace(frase,'-',' ') 
    
    if ',' in frase:
        frase = str.replace(frase,',',' ') 
    
    if ':' in frase:
        frase = str.replace(frase,':',' ') 
    
    if ';' in frase:
        frase = str.replace(frase,';',' ') 
    
    elif '.' in frase:
        frase = str.replace(frase,'.',' ') 
        
    elif '!' in frase:
        frase = str.replace(frase,'!',' ') 
        
    elif '?' in frase:
        frase = str.replace(frase,'?',' ') 
        
    frase = str.lower(frase)
    frase = list.reverse(frase)
       
    return frase