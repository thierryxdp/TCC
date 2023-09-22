def posLetra(frase,letra,pos):
    txt = frase
    antes= pos-1
    
    local = txt.find(letra,antes)
    return local