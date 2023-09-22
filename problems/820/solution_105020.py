def posLetra(frase,letra,num):
    qnt_letra=0
    for letra in frase:                
        qnt_letra+= 1
        if qnt_letra < num:
            return -1
        else:
            return frase.count(letra)