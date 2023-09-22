def lingua_p(texto):
    frase=''
    for letra in texto:
        if letra in'AEIOUaeiouáéíóúÁÉÍÒÙ':
            frase=frase+str.lower(letra)+'p'+str.lower(letra)
        else:
            frase=frase+str.lower(letra)
    return frase