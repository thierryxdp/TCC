def uppCons(frase):
    'dada uma frase retorne todas consoantes em maiusculo.str--str'
    frasec=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz' :
            frase=frase + str.upper(frase[i])
        i=i+1
    return frase