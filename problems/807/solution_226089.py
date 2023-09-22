def conta_frases(texto):
    """retorna o número de palavras em uma frase. (str->int)"""
    texto = str.replace(texto,"!",".")
    texto = str.replace(texto,"?",".")
    texto = str.replace(texto,"...",".")
                        
    frases = str.split(texto,". ")
    
    
    return len(frases)