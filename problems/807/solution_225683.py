def conta_frases(texto):
    '''Função que conta a quantidade de frases que aparecem
    no texto de entrada
    '''
   
    
    texto1=texto.replace('?','.')
    texto2=texto1.replace('!','.')
    texto3=texto2.replace('...','.')
    
        
    
    
    return texto3.count(.)