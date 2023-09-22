def conta_frases(texto):
    """
    Código que conta um número de frases que aparecem em um texto
    :entrada --> string:
    :return --> int:
    """
    if ('.' or '!' or '?' in texto):
        return (texto.split('?')) 
    if ('?' not in texto): 
        return (texto.split('!'))
    
    #if ('.' or '...' or '!' or '?' in texto):   
    #    return (texto.split('.'))
    return