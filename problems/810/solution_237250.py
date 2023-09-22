def inverte(texto):
    texto = str.replace(texto,"."," ")
    texto = str.replace(texto,";"," ")
    texto = str.replace(texto,":"," ")
    texto = str.replace(texto,"-"," ")
    texto = str.replace(texto,"?"," ")
    texto = str.replace(texto,"-"," ")
    texto = str.replace(texto,"!"," ")
    return texto