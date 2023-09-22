def conta_frases(frases):
    """Dado um texto armazenado em uma string, a função retorna o número de frases que aparecem no texto."""
    """str->int"""
    return str.count(frases,". ",0,len(frases)) + str.count(frases,"!",0,len(frases)) + str.count(frases,"?",0,len(frases)) + str.count(frases,"...",0,len(frases))