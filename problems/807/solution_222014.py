def conta_frases(texto):
    ''' Função que conta quantas frases
        aparecem em um dado texto 
        str -> int '''
    
    texto1, texto2, texto3, texto4 = [], [], [], []
    
    if '!' in texto: 
        texto1 = texto.split('!') 
    if '.' in texto: 
        texto2 = texto.split('.') 
    if '?' in texto: 
        texto3 = texto.split('?') 
    if '...' in texto: 
        texto4 = texto.split('...') 
        
    return len(texto1 + texto2 + texto3 + texto4)