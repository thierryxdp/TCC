def uppCons(frase):
    maius=''
    i=0
    while i<len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            maius=frase[i].upper
        else:
            maius=frase[i]
        i=i+1
    return maius