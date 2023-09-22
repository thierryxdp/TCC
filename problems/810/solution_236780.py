def inverte(frase):
    '''descrição'''
    frase = str.replace(frase,", "," ")
    frase= str.replace(frase,":"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,"/"," ")
    frase=str.split(invertida, " ")
    invertida = frase[-1::-1]
    str.join(" ",invertida)
    return invertida