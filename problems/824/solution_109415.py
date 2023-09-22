def uppCons(frase):
    contador=0
    frase_nova=''
    while contador<len(frase):
        if frase[contador] in "bcçdfghjklmnpqrkstvxwz":
            frase_nova=frase_nova+str.upper(frase[contador])
        else:
            frase_nova=frase_nova+frase[contador]
        contador=contador+1
    return frase_nova