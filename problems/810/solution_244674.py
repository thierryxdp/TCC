def inverte(texto):
    texto = str.lower(texto)
    texto = texto[0:-1]
    texto = str.replace(texto, "," , "")
    texto = str.split(texto,)
    texto = list.reverse(texto)
    
    
    return texto