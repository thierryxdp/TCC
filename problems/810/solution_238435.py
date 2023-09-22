def inverte(frase):
    """"""
    f=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'!',' '),'.',' '),'?',' ')
    list.reverse(f)
    return str.join(' ',f)