def conta_frases(frase):
    """Dado um texto armazenado em uma string, retorna o numero de frases que aparecem neste texto.
    str->int"""
    frase = frase.replace("...",".") 
    return frase.count('!') + frase.count('?') + frase.count('.')