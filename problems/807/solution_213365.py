def conta_frases(frase):
    """Dado um texto armazenado em string, faça umafunção que conta a quantidade de frases contidas nesse texto """
          
    frase1 = len( ".", " ")
    frase2 = len( "...", " ")  
    frase3 = len( "?", " ")
    frase4 = len( "!", " ")
    
    frase  = str.lower(frase4)
    frase  = str.split(texto, " ")
    string = str.join(" ", frase)
    return string