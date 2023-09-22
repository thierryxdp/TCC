def inverte(frase):
    frase=str.replace(frase,"," , " ")
    frase=str.replace(frase,"!" , " ")
    frase=str.replace(frase,"?" , " ")
    frase=str.replace(frase,":" , " ")
    frase=str.replace(frase,";" , " ")
    frase=str.replace(frase,"." , " ")
    frase=frase.lower(frase)
    frase=frase.splt()
    frase=frase[-1::-1]
    frase=" ".join(frase)
    return frase