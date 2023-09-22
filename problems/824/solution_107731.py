def uppCons(frase):
    i=0
    cons=''
    while i<len(frase):
        if frase[i] in 'qwrtypsdfghjklçzxcvbnm':
            cons= frase.upper()
        i=i+1
    return cons