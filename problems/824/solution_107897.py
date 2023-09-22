def uppCons (frase):
    """funcao que retorna a frase inserida com as consoantes maiusculas e o 
       restante exatamente como estava
       
       str -> str
    """
    vogais= "aeiouAEIOU"
    i=0
    
    while i<len(frase):
        if frase[i] in vogais:
            str.upper(frase[i])
        i = i+1
        
    return frase