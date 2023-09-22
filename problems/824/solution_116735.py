def uppCons(frase):
    i=0
    maiusculo=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            maiusculo += str.upper(frase[i])
        i=i+1
    return maiusculo