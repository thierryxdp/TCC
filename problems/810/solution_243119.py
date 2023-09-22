def inverte(texto):
    texto = str.replace(texto, "-"," ")
    texto = str.replace(texto, ","," ")
    texto = str.replace(texto, ":"," ")
    texto = str.replace(texto, ";"," ")
    texto = str.replace(texto, "."," ")
    texto = str.replace(texto, "?"," ")
    texto = str.replace(texto, "!"," ")
    texto = str.replace(texto, "..."," ")
    
    
    lista = str.split(texto)
    
    
    
    return str.join(" ",lista[::-1])