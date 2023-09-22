def lingua_p(palavra):
    """A função recebe como entrada uma string em português e retorna
    a palavra em forma de string na sua tradução para língua do P.
    str -> str"""
    
    frase = ""
    
    for letra in palavra:
        
        if letra not in "aAeEiIoOuU":
            frase = letra
            
    	elif letra in "aA":
            frase = frase + "apa"
        
        elif letra in "eE":
            frase = frase + "epe"
            
        elif letra in "iI":
            frase = frase + "ipi"
            
        elif letra in "oO":
            frase = frase + "opo"
            
        elif letra in "uU":
            frase = frase + "upu"
    
    return str.lower(frase)