def inverte(frase):
    frase1=str.lower(str.replace(str.replace(str.replace(frase,'.',' '),',',' '),'!',' '))
    return list.reverse(frase1)