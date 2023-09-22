def uppCons(frase):
    maius=''
    i=0
    while i<len(frase):
        if frase[i] in 'QWERTYUIOPASDFGHJKLÇCVBNMZX':
            maius=maius+frase[i]
        i=i+1
    return maius