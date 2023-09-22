def conta_frases(frase):
    """função que dado um texto armazenado em uma string, retorna o número de frases que
    aparecem neste texto  str -> int"""
    
    frase = frase.replace("...", ".")
    frase = frase.replace("?", ".")
    frase = frase.replace("!", ".")
    frase = frase.split(".")
    
    return len(frase)-1