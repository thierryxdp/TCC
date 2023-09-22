def inverte(frase):
    a = frase
    a = str.replace(a,'...','')
    a = str.replace(a,',','')
    a = str.replace(a,'!','')
    a = str.replace(a,'.','')
    a = str.replace(a,'?','')
    a = str.replace(a,'—','')
    a = str.replace(a,':','')
    a = str.replace(a,';','')
    a = str.replace(a,'-','')
    a = str.lower(a)
    a = str.split(a)
    a = tuple(a)
    a = a[0:-1]
    a = list(a)
    a = str.join(" ",a)
    return a