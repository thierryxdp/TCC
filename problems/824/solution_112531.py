def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            cons=frase[i]
            cons=cons.upper()
        i=i+1
        return cons