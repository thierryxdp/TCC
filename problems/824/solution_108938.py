def uppCons(frase):
    i=0
    r=''
    while i<len(frase):
        if frase[i] in 'ÃÂÁÀAÊÉÈEÎÍÌIÔÕÓÒOÛÚÙUâãáàaêéèeîíìiôõóòoûúùu':
            r=r+frase[i]
        else:
            r=r+frase[i].upper
        i=i+1
    return r