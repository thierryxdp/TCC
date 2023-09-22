def inverte(texto):
    texto = str.replace(texto,","," ")
    texto = str.replace(texto,"."," ")
    texto = str.replace(texto,";"," ")
    texto = str.replace(texto,":"," ")
    texto = str.replace(texto,"-"," ")
    texto = str.replace(texto,"?"," ")
    texto = str.replace(texto,"-"," ")
    texto = str.replace(texto,"!"," ")
    texto = str.lower (texto)
    texto = str.split(texto, '  ')
    
    return texto