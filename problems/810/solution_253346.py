def inverte(frase):
    frase=frase.replace("..."," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("."," ")
    frase=frase.replace("-"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace(":"," ")
    frase=frase.replace(","," ")
    lista=frase.split(" ")
    nl = []
    contador = len(lista)-1
    while contador>=0:
        nl.append(lista[contador])
        contador= contador - 1
    novo=''
    for i in nl:
        novo=novo + " " + i  
    return novo