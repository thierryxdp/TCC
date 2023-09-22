def inverte(frase):
    a= frase_com_espaco(frase)
    b= str.split(a," ")
    c= list.reverse(b)
    d= str.join(" ",b)
    e= str.lower(d)
    return e