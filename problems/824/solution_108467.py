def uppCons(frase):
    i=0
    novo=""
    while i<len(frase):
        if frase[i] in "qwrtypsdfghjklçzxcvbnm":
            frase=str.upper(frase[i])
        i=i+1
    return frase