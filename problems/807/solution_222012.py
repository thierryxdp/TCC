def conta_frases(texto):
    ''' Função que conta quantas frases
        aparecem em um dado texto 
        str -> int '''
    
    if '!' in texto: 
        texto = texto.split(!) 
    if '.' in texto: 
        texto = texto.split(.) 
    if '?' in texto: 
        texto = texto.split(?) 
    if '...' in texto: 
        texto = texto.split(...) 
        
    return len(texto)