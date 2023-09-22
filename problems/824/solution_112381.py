def uppCons(frase):
    i = 0
    newfrase = frase
    while i < len(frase):
        if newfrase[i] != 'a':
            str.upper(newfrase[i])
        	i+=1
    return newfrase