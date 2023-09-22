def uppCons(frase):
    contador=0
    while contador+1<len(frase):
        if frase[contador] not in  "aeiouãéêíóôõ" :
            frase=frase.replace(frase[contador],frase[contador].upper())
        contador+=1
    return frase