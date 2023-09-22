def inverte(frase):
    f=str.replace(str.replace(str.replace(str.replace(frase,'.',' '),',',' '),'!',' '),'?',' ')
    return f[::-1]