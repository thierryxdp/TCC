def uppCons(frase):
    i=0
    i_c=0
    conso='qwrtypsdfghjklzxcvbnmç'
    while i<len(frase)and i_c<len(conso):
        if conso[i_c]in frase:
            conso_frase=frase[frase.index(conso[i_c])]
            frase=frase.replace(conso_frase,conso_frase.upper())
        i_c+= 1
        i+=1
        if i>=len(frase):
            i=0
    return frase