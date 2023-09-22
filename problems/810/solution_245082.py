def inverte(frase):
    
    """
    Retorna uma frase sem letras maiusculas, sem pontuacao e na ordem 
    inversa da que foi escrita inicialmente;
    str -> str
    """
    
    frase = frase.replace("."," ") 
    frase = frase.replace("..."," ")
    frase = frase.replace(","," ")
    frase = frase.replace("?"," ") 
    frase = frase.replace("!"," ")
    frase = frase.replace(":"," ")
    frase = frase.replace(";"," ")
    frase = frase.replace("-"," ")
    frase1 = list(frase)
    reverso = frase1.reverse
    SREV = str(reverso)
    SM = SREV.lower
    return SM