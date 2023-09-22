def inverte(f):
    lista_palavras =str.split(f,' ')
    lista_invertida =lista_palavras[::-1]
    f_contrario =str.join(' ',lista_invertida)
    return str.replace(str.replace(str.replace(str.replace(str.lower(f_contrario),',',''),'.',''),'!',''),'?','')