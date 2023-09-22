def uppCons(frase):
    i=0
    final=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxzç':
            final=final.append(frase[i].upper())
        else:
            final=final.append(frase[i])
        i=i+1
        return final