def posLetra(frase,letra,pos):
    txt = frase
    antes= pos-1
    depois = pos+1
    local = txt.find(letra,antes,depois)
    return local