def conta_frases (texto):
    '''
        Dado um texto a string retorna quantas frases o texto
        possui
        str -> int
    '''
    if '.' in texto:
        final = str.count(texto, str.split('.'))
    if '!' in texto:       
        exclamacao = str.count(texto, str.split('!'))
    if '?' in texto:
        interrogacao = str.count(texto, str.split('?')) 
    if '...' in texto:
        reticencias = str.count(texto, str.split('...'))
        return final + exclamacao + interrogacao + reticencias