def uppCons(frase):
    i=0
    final=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxzç':
            final=''.join(frase[i].upper())
        else:
            final=''.join(n for n in frase[i] if n != 'bcdfghjklmnpqrstvwxzç')
        i=i+1
        return final