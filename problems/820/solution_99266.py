def posLetra(frase,letra,pos):
    txt = frase
    if txt.count(letra) < pos:
        return -1
    
    antes= pos-1
    
    local = txt.find(letra,antes)
    return local