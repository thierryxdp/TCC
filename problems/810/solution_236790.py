def inverte(frase):
    '''descrição'''
    frase = str.replace(frase,", "," ")
    frase= str.replace(frase,":"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"- "," ")
    frase = str.replace(frase,"/"," ")
    frase_semespaço=str.split(frase_semespaço, " ") 
    invertida = frase_semespaço[-1::-1]
    frase_invertida=str.join(" ",invertida)
    return frase_invertida