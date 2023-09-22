def inverte(frase):
    """Retorna a frase fornecida invertida;
    str -> str"""
    frase = str.replace(frase, "!", " ")
    frase = str.replace(frase, "?", " ")
    frase = str.replace(frase, ".", " ")   
    frase = str.replace(frase, ",", " ")    
    frase = str.replace(frase, "-", " ")    
    frase = str.replace(frase, ":", " ")    
    frase = str.replace(frase, ";", " ")
   	
    v1 = str.split(frase, " ")
    v2 = str.join(" ", v1)
    
    return v2[-1::1]