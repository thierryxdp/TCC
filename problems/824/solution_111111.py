def uppCons(frase):
    i=0
    C=''
   
    while i < len(frase):
        if frase[i] not in 'hdbsjssjss':
            C=C+str.upper(frase[i])
        else:
            C=C+frase[i]
            i=i+1
    return C