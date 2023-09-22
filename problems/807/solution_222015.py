def conta_frases(texto):
    ''' Função que conta quantas frases
        aparecem em um dado texto 
        str -> int '''
    
    texto1 = texto.split('.')
    texto2 = texto.split('!')
    texto3 = texto.split('?')
    texto4 = texto.split('...')
    
    if '.' not in texto:
        texto1 = []
    if '!' not in texto:
        texto2 = []
    if '?' not in texto:
        texto3 = []
    if '...' not in texto:
        texto4 = []
        
    return len(texto1 + texto2 + texto3 + texto4)