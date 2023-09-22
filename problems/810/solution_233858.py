def inverte(f):
    lista_palavras =str.split(f,' ')
    invertida =lista_palavras[::-1]
    contrário = str.join(' ',invertida)
    return str.replace(str.replace(str.replace(str.replace(str.lower(contrário),',',''),'.',''),'!',''),'?','')