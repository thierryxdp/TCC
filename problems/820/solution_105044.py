def posLetra(frase,letra,num):
    for letra in frase:                
        if str.count(frase, letra) < num:
            return -1
        else:
            return frase.find(letra)