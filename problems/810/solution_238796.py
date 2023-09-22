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
    v1 = v1[::-1]
    v2 = str.join(" ", v1)
    v3 = str.lower(v2)
    
    return str.lstrip(v3)