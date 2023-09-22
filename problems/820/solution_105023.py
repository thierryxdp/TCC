def posLetra(frase,letra,num):
    for letra in frase:                
        if frase.count(letra) < num:
            return -1