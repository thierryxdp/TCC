def conta_frases(texto):
    """função retorna o numero de frases que aparece em um texto armazenado 
       em uma string - string -> int"""
    frase1 = str.count(texto, '.')
    frase2 = str.count(texto, '!')
    frase3 = str.count(texto, '?')
    frase4 = str.count(texto, '...')
    
    return (frase1 + frase2 + frase3 + frase4) - frase4*3