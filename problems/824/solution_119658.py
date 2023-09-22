def  uppCons(frase):
    i=0
    s=''
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvxwyz':
            s+=str.upper(frase[i])
        else:
            s+=frase[i]
        i=i+1 
    return s