def inverte(frase):
    frase=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'!',' '), '?',' '),'.',' '), '-',' '), ',',' '), ':',' '), ';',' ')
    frase=str.lower(frase)
    lista=frase.split()
    str_final= str.join(lista[::-1]," ")
    return str_final