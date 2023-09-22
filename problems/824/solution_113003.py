def uppCons (frase):
    i=0
    fraseF=''
    consoante='bcdfgjklmnpqrstvwxz'
    CONSOANTE=consoante.upper()
    while i < len(frase):
        if frase[i] in 'bcdfgjklmnpqrstvwxz':
            CONSOANTE=consoante.upper()
            fraseF=frase[i]
        i=i+1
    return fraseF