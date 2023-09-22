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
   	v2 = list(v1[::-1])
    v3 = str.join(" ", v2)
    v4 = str.lower(v3)
    
    return str.lstrip(v4)