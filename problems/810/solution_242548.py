def inverte(texto):
    texto=str.split(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto,'-',' '),',',' '),':',' '),'.',' '),'?',' '),'!',' '))
    list.reverse(texto)
    return str.lower(str.replace(str.replace(str.strip(str.strip(str(texto),'['),']'),',',''),"'",''))