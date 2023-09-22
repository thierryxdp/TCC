def uppCons(frase):
    frase=[]
    i=0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            list.append(frase,upper[i])
        i=i+1
    return frase