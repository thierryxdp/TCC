def inverte(frase):
    '''Função que troca todas as pontuações de uma frase por espaços;
    str -> str'''
    
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
              

    frase = frase.lower()
    
    return frase.reverse()