def uppCons(frase):
    i=0
    cons=''
    while i<len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            cons= str.upper(frase[i])
        i=i+1
    return cons