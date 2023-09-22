def inverte(frase):

    s = frase

    s1 = str.replace(s,'-',' ')
    s2 = str.replace(s1,',', ' ')
    s3 = str.replace(s2, ':',' ')
    s4 = str.replace(s3, ';', ' ')
    s5 = str.replace(s4,'.',' ')
    s6 = str.replace(s5,'!',' ')
    s7 = str.replace(s6,'?',' ')

    L= str.split(s7,'')
    L2 = L[::-1]
    L3 = str.join('',L2)
    Lista_invertida = str.lower(L3)
    
    return Lista_invertida