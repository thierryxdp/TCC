def conta_frases(texto):
    """retorna o número de frases em um texto. (str->int)"""
    texto = str.replace(texto,"!",".")
    texto = str.replace(texto,"?",".")
    texto = str.replace(texto,"...",".")
                        
    frases = str.split(texto,". ")
    
    
    return len(frases)