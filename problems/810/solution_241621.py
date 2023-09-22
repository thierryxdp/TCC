def inverte(frase):
    f=str.split(str.lower(str.replace(str.replace(str.replace(str.replace(frase,'.',' '),',',' '),'!',' '),'?',' ')))
    return str.replace(f[::-1],',',' ')