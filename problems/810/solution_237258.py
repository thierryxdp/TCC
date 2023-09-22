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
    texto = str.split(texto, ' ')
    tetxo = texto[len(texto):-1: 0]
    
    return texto