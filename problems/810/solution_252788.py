def inverte(frase):
    frase = str.replace(frase,";","")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,"."," ")
    nova_frase = str.lower(frase)
    return frase