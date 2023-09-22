def inverte(texto):
    texto = str.replace(texto, "-","")
    texto = str.replace(texto, ",","")
    texto = str.replace(texto, ":","")
    texto = str.replace(texto, ";","")
    texto = str.replace(texto, ".","")
    texto = str.replace(texto, "?","")
    texto = str.replace(texto, "!","")
    texto = str.replace(texto, "...","")
    
    
    list.sort(str.split(texto), reverse=True)
    
    
    
    return str.join(" ",texto)