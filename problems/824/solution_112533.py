def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            cons=frase[i]
            cons=cons.upper()
            frase.replace(frase[i],cons)
        i=i+1
        return frase