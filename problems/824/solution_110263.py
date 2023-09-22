def uppCons(frase):
    i=0
    final=''
    while len(final)<len(frase:
        if frase[i] in 'bcdfghjklmnpqrstvwxzç':
            final=final.join(frase[i].upper())
        else:
            final=final.join(frase[i])
        i=i+1
        return final