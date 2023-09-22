def uppCons(frase):
    ind=0
    while ind<len(frase):
        if frase[ind] in 'AEIOUaeiou':
            pass
        else:
            str.upper(frase[ind])
        ind+=1
    return frase