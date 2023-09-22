def inverte(frase):
    x=str.lower(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'.',' '),'?',' '),'!',' '))
    y=list.reverse(str.split(x))
    return y