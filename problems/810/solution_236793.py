def inverte(frase):
    '''descrição'''
    frase = str.replace(frase,", "," ")
    frase= str.replace(frase,":"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,"/"," ")
    frase=str.split(frase, " ") 
    invertida = frase[-1::-1]
    frase_invertida=str.join(" ",invertida)
    str.strip(frase_invertida)
    return frase_invertida