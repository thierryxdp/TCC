def inverte(texto):
    texto = str.replace(texto, "-"," ")
    texto = str.replace(texto, ","," ")
    texto = str.replace(texto, ":"," ")
    texto = str.replace(texto, ";"," ")
    texto = str.replace(texto, "."," ")
    texto = str.replace(texto, "?"," ")
    texto = str.replace(texto, "!"," ")
    texto = str.replace(texto, "..."," ")
    
    
    
    
    listaR = list.sort(str.split(texto), True)
    
    return listaR