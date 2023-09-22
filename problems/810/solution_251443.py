def inverte(frase):
    str.lower(frase)
    str.replace(frase,'.','')
    str.replace(frase,',','')
    frase=str.split(frase)
    list.reverse(frase)
    return=str.join(' ',frase)