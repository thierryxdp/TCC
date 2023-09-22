def uppCons(frase):
    i=0
    final=''
    while 1<10:
        if frase[i] in 'bcdfghjklmnpqrstvwxzç':
            final=final.join(frase[i].upper())
        else:
            final=final.join(frase[i])
        i=i+1
        return final