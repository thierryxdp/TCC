def lingua_p(palavra):
    """função que dado uma palavra, retorna a mesma convertida na lingua do P, ou seja, a letra p é incluída após  cada vogal mais a vogal original. Entrada -> str; Saída -> str"""
    
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