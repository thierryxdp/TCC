def posLetra(frase,letra,occ):
    
    frase = frase.replace(letra,' ',occ-1)
    return frase.find(letra)