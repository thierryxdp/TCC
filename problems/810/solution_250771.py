def inverte(frase):
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,"."," ")
    frase=str.lower(frase)
    return frase