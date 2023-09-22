def uppCons(frase):
    frase2=''
    contador=0
    tamlista=len(frase)
    
    while contador<tamlista:
        if frase[contador] in 'bcdfghjklmnpqrstvwxyz':
            frase2=frase2 + str.upper(frase[contador])
    return frase2