def posLetra(frase,letra,pos):
        
    local = frase.index(letra,pos-1,pos+1)
    return local