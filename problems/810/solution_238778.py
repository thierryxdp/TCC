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
    v3 = str.lower(v2)
    v3 = str.lstrip
    
    return v3[::-1]