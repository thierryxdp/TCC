def uppCons(frase):
    i = 0
    newfrase = frase
    while i < len(newfrase):
        if newfrase[i] != 'a':
            str.upper(newfrase[i])
        i+=1
    return newfrase