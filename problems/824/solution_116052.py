def uppCons(frase):
    'dada uma frase retorne todas consoantes em maiusculo.str--str'
    frasec=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç' :
            frasec=frasec+str.upper(frase[i])
        else :
            frasec=frasec+frase[i]
        i=i+1
    return frasec