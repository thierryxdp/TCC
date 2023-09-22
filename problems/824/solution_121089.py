def uppCons(frase):
    frase2=''
    contador=0
    tamlista=len(frase)
    
    while contador<tamlista:
        if frase[contador] in 'bcdfghjklmnpqrstvwxyzç':
            frase2=frase2 + str.upper(frase[contador])
        else:
            frase2=frase2 + frase[contador]
        contador=contador + 1
    return frase2