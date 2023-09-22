def posLetra(frase,letra,num):
    x=letra
    for letra in frase:                
        if frase.count(letra) < num:
            return -1
        else:
            return frase.find(x,num)