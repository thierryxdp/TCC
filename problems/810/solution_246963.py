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
        
        return frase
        
        
        def inverte (frase1):
            '''retorna a frase na ordem inversa, sem pontuação 
            e sem letras maiúsculas
            str -> str'''
            
            frase1 = frase1.lower()
            lista = frase1. split()
            
            return lista.reverse()