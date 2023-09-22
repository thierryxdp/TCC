def uppCons(frase):
    frase=list(frase)
    i=0
    while i<len(frase):
        if frase[i] in "qwrtypsdfghjklçzxcvbnm":
            frase="".join(frase)
            novo=str.upper(frase[i])
            frase=list(frase)
            del frase[i]
            list.insert(frase,i,novo)
        i=i+1  

    frase="".join(frase)        
    return frase