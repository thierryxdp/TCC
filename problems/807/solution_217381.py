def conta_frases(texto):
    """Conta o número de frases que aparecem nesse texto"""
    """str -> int"""
    
   texto = str(texto)
    
    return texto.count("."[0:len(texto)]) - 3 * texto.count("..."[0:len(texto)]) + texto.count("!"[0:len(texto)]) + texto.count("?"[0:len(texto)]) + texto.count("..."[0:len(texto)])