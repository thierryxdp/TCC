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
    lista=lista.reverse()
    novo=''
    for i in lista:
        novo=novo + " " + i  
    return novo