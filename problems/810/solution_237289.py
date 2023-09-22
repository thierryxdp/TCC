def inverte(texto):
    texto = str.replace(texto,","," ")
    texto = str.replace(texto,"."," ")
    texto = str.replace(texto,";"," ")
    texto = str.replace(texto,":"," ")
    
    texto = str.replace(texto,"?"," ")
    texto = str.replace(texto,"-"," ")
    texto = str.replace(texto,"!"," ")
    texto = str.lower (texto)
    texto = str.split(texto,' ')
    texto = texto[::-1]
    texto = str.join(" ",texto)
    
    
    
    
    return str.lstrip(texto)