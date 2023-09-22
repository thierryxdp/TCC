def uppCons(frase):
    maius=''
    i=0
    while i<len(frase):
        if frase[i] in 'QWERTYUIOPASDFGHJKLÇZXCVBNM':
            maiuss=maius+frase[i]
        i+=i+1
    return maius