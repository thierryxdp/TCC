def uppCons(frase):
    p=0
    f=''
    while p<len(frase):
        if frase[p] in 'bcçdfghjklmnpqrstvwwyz':
            f= f+str.upper(frase[p])
            p+= 1
        else:
            f=f+frase[p]
            p+=1
    return f