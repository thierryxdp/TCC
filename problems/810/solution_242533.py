def inverte(texto):
    texto=str.split(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto,'-',' '),',',' '),':',' '),'.',' '),'?',' '),'!',' '))
    list.reverse(texto)
    return str.strip(str.strip(str(texto),'['),']')