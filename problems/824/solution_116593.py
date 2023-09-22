def uppCons(frase):
    ''' str -> str'''
    i=0
    x=''
    y='AEIOUaeiouáóêãõúíé'
    while i<len(frase):
        if frase[i] not in y:
            x+=str.upper(frase[i])
        else:
            x+=frase[i]
        i+=1
    return x