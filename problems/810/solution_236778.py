def inverte(frase):
    '''descrição'''
    frase = str.replace(frase,", "," ")
    frase= str.replace(frase,":"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,"/"," ")
    invertida = frase[-1::-1]
    str.split(frase, " ")
    str.join(" ",frase)
    return frase