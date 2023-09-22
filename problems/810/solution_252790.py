def inverte(frase):
    frase = str.replace(frase,";","")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,"."," ")
    nova_frase = str.lower(frase)
    lista=str.split(nova_frase,' ')
    nova_lista=lista[::-1]
    return str.join(" ", nova_lista)