def conta_frases(texto):
    
    ''' Função que conta quantas frases
        aparecem em um dado texto.
        str -> int '''
    
    
    texto = texto.replace('...', '/')
    
    ponto = texto.count('.') 
    reticencias = texto.count('/') 
    interrogacao = texto.count('?') 
    exclamacao = texto.count('!') 
    
    return ponto + reticencias + interrogacao + exlamacao