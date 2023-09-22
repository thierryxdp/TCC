def lingua_p(palavra):
    """A função recebe como entrada uma string em português e retorna
    a palavra em forma de string na sua tradução para língua do P.
    str -> str"""
    
    frase = ""
    
    for letra in palavra:
        
        if letra not in "aáAÁeéEÉiíIÍoóOÓuúUÚ":
            frase = frase + letra
            
    	elif letra in "aáAÁ":
            frase = frase + letra + "p" + letra
        
        elif letra in "eéEÉ":
            frase = frase + letra + "p" + letra
            
        elif letra in "iíIÍ":
            frase = frase + letra + "p" + letra
            
        elif letra in "oóOÓ":
            frase = frase + letra + "p" + letra
            
        elif letra in "uúUÚ":
            frase = frase + letra + "p" + letra
    
    return str.lower(frase)