def inverte(texto):
    texto = str.lower(texto)
    texto = texto[0:-1]
    texto = str.replace(texto, "," , "")
    novo = texto[-1:]
    
    return texto