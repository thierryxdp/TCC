def posLetra(frase,letra,pos):
    antes= pos-1
    depois = pos+1
    local = frase.index(letra,antes,depois)
    return local