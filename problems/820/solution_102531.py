def posLetra(frase, letra, numero):
    i = 0
    
    if numero > len(frase):
        return -1
    while numero <= len(frase):
         s = frase.find(letra)
    return s