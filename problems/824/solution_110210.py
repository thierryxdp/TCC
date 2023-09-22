def uppCons(frase):
    i=0
    final=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxzç':
            final=''.join(frase[i].upper())
        if not:
            final=''.join(frase[i])
        i=i+1
        return final