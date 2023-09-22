def conta_frases(texto):
    '''Função que conta a quantidade de frases que aparecem
    no texto de entrada
    '''
   
    texto1=''
   
    
    if '?' in texto:
        texto1=texto.replace('?','.')
        
    elif '!' in texto:
        texto2=texto1.replace('!','.')
        
    elif '...' in texto:
        texto3=texto2.replace('...','.')
    
        
    
    
    return texto3.count(.)