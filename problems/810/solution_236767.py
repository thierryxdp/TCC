def inverte(frase):
    '''descrição'''
    frase = str.replace(frase,","," ")
    frase= str.replace(frase,":"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,"/"," ")
    str.split(frase, " ")
    str.join(" ",[frase])
    return frase