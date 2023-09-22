def uppCons(frase):
    x=str.upper(frase)
    i=0
    while i<len(x):
        if x[i] in 'AEIOU':
            y=x[i]
            x[i]=str.lower(y)
        i=i+1
    return x