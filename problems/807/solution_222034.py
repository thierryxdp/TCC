def conta_frases(texto):
    
    ''' Função que conta quantas frases
        aparecem em um dado texto.
        str -> int '''
    
    
    texto = texto.replace('.', '/')
    
    return texto.count('!') + texto.count('?') + texto.count('/')