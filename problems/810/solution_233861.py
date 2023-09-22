def inverte(f):
    lista =str.split(f,' ')
    invertida =lista[::-1]
    contrário = str.join(' ',invertida)
    return str.replace(str.replace(str.replace(str.replace(str.lower(contrário),',',''),'.',''),'!',''),'?','')