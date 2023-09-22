def uppCons(frase):
    ''' Uma função que dada uma frase retorne todas as consoantes em letras maíusculas;str->str'''
    cons=bcdfghjklmnpqrstvwxyz
    i=0
    while i<len(frase):
        if frase[i] in cons:
            str.upper(frase)
        i=i+1
    return frase