def uppCons(x):
    i=0
    frase=''
    while i<len(x):
        if x[i] in 'qwrtypsdfghjklçzxcvbnm':
            frase+=str.upper(x[i])
        else:
            frase+=x[i]
        i+=1
    return frase