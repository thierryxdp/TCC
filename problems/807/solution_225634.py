def conta_frases(texto):
    '''Função que conta a quantidade de frases que aparecem
    no texto de entrada
    '''
   
    
    if '.' in texto:
        texto=texto.split('.')
    
    elif '?' in texto:
        texto=texto.split('?')
        
    elif '!' in texto:
        texto=texto.split('!')
        
    elif '...' in texto:
        texto=texto.split('...')
        
    elif ';' in texto:
        texto=texto.split(';') 
        
    elif ' ' in texto:
        
    return texto