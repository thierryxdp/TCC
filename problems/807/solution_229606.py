def conta_frases (texto):
    '''
        Dado um texto a string retorna quantas frases o texto
        possui
        str -> int
    '''
    if '.' in texto:
        final = str.count(str.split('.'))
    if '!' in texto:       
        exclamacao = str.count(str.split('!'))
    if '?' in texto:
        interrogacao = str.count(str.split('?')) 
    if '...' in texto:
        reticencias = str.count(str.split('...'))
        return final + exclamacao + interrogacao + reticencias