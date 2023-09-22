def inverte(frase):
    frase=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'!',' '), '?',' '),'.',' '), '-',' '), ',',' '), ':',' '), ';',' ')
    frase=str.lower(frase)
    lista=frase.split()
    for i in range(len(lista)):
        str_final= str.join(lista[i], " ")
    return str_final