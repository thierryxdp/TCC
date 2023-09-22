def conta_frases(texto):
    '''Função que conta a quantidade de frases que aparecem
    no texto de entrada
    '''
   
    
   
    
    if '?' in texto:
        texto=texto.replace('?','.')
        
    if '!' in texto:
        texto=texto.replace('!','.')
        
    if '...' in texto:
        texto=texto.replace('...','.')
        
    if ';' in texto:
        texto=texto.replace(';','.')
        
                
    return len(texto.split('.'))