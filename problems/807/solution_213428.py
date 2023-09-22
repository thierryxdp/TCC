def conta_frases(text):
    """
    
    """
    texto = text.count('.') + text.count('?') + text.count('!') - 2 * text.count('...')
     
    return  texto