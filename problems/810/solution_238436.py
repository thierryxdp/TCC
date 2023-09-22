def inverte(frase):
    """"""
    f=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'!',' '),'.',' '),'?',' ')
    f=str.split(f)
    list.reverse(f)
    return str.join(' ',f)