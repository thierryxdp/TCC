def inverte(texto):
    s=str(texto)
    f=str.replace(s,"...",".")
    j=str.replace(f,"-"," ")
    o=str.replace(j,","," ")
    g=str.strip(o,"?!.;:")
    h=g[:]+" "
    lista=str.split(h)
    lista2=lista[::-1]
    return str.lower(lista2)