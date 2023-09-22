def conta_frases (texto):
    '''
        Dado um texto a string retorna quantas frases o texto
        possui
        str -> int
    '''
    if '.' in texto:
        final = len(str.split('.'))  
    if '!' in texto:       
        exclamacao = len(str.split('!'))
    if '?' in texto:
        enterogacao = len(str.split('?')) 
    if '...' in texto:
        reticencias = len(str.split('...'))
        return final + exclamacao + enterogacao + reticencias