def posLetra(frase,letra,num):
    for letra in frase:                
        qnt_letra+= 1
        if frase.count(letra) < num:
            return -1
        else:
            return frase.count(letra)