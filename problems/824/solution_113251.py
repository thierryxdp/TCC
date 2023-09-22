def uppCons(frase):
    i=0
    string=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz,.,...,:,!,?,-,/,':
            string=string+frase[i].upper()
        else:
            string=string+frase[i]
        i=i+1
    return string