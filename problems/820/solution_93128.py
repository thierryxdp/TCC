def posLetra(frase,letra,oc):
    X=frase.count(letra)
    if X<oc:
        return -1
    if X>=oc:
        for c in frase:
            a=frase.index(letra)
            b=frase.index(letra,a+1)
                    
        return b