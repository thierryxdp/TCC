def uppCons(frase):
    a=0
    while a< len(frase):
        if frase[a] in 'bcdfghjklmnpqrstvwxyzç':
            frase= frase + frase.replace(frase[a], frase[a].upper())
        a=a+1
    return frase