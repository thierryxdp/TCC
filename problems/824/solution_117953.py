def uppCons(frase):
    maius=''
    i=0
    while i<len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            maius=frase[i].upper()
        i=i+1
    return maius