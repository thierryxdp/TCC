def conta_frases(texto):
    """Dado um texto retorna o número de frases nele contido.
       str -> int"""
    
    if len(texto.split('.')):
        result1 = ()
    elif len(texto.split('!')):
        result2 = ()
    elif len(texto.split('?')):
        result3 = ()
    elif len(texto.split('...')):
        result4 = ()
        
    return min(result1, result2, result3, result4)