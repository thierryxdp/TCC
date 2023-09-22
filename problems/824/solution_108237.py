def uppCons(frase):
    indice=0
    frase_nova=''
    while indice<len(frase):
        if frase[indice] not in 'aeiouAEIOUáãàéíõóúÁÃÀÉÍÕÓÚ':
            frase_nova+=frase[indice].upper()
        else:
            frase_nova+=frase[indice]
        indice+=1
    return frase_nova