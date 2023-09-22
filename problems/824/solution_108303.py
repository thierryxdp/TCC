def uppCons(frase):
    ind=0
    novaFrase=''
    while ind<len(frase):
        if frase[ind] in 'AEIOUaeiou':
            novaFrase=novaFrase+frase[ind]
        else:
            novaFrase=novaFrase+str.upper(frase[ind])
        ind+=1
    return frase