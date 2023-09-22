def uppCons(f):
    ''
    vogal='aAeEiIoOuU' 
    prox=0
    nova=''
    while prox<len(f):
        if f[prox]!=vogal:
            str.upper(f[prox])
            nova= nova+f[prox]
        else:
            nova= nova+f[prox]
        prox=prox+1
    return nova