def uppCons(frase):
    i=0
    final=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxzç':
            final=final.join(frase[i].upper())
        else:
            final=final.join(frase[i])
            i=i+i
        
        return final