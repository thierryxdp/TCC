def inverte(texto):
    exc = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto,'.',''), ',',''),':',''),';',''),';',''),'!',''),'?',''),'...',''),'-',' ')                                                                                              
    sep = list(str.split(exc," "))
    inversa = sep[-1:0:-1]
    return str.lower(str.join(" ",inversa))