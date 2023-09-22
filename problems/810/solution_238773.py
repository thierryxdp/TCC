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
   	frase1 = str.lower(frase)
    
    v1 = str.split(frase1, " ")
    v2 = str.join(" ", v1)
    v3 = v2[::-1]
    
    return v3