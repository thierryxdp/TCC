def uppCons(frase):
    contador = 0
    while contador<len(frase):
        if frase[contador]=='a':
            frase[contador] = 'A'
        if frase[contador]=='e':
            frase[contador]=='E'
        if frase[contador]=='i':
            frase[contador] = 'I'
        if frase[contador]=='o':
            frase[contador] = 'O'
        if frase[contador]=='u':
            frase[contador] = 'U'
        contador = contador + 1
    return frase