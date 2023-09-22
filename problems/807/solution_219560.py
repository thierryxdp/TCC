def conta_frases(frase):
    """Função que conte e retorna o número de frases que aparecem neste 
    texto
    str-> int"""
    
    f1 = frase.str(".")
    f2 = frase.str("!")
    f3 = frase.str("?")
    f4 = frase.str("...")
    
    return f1+f2+f3+f4