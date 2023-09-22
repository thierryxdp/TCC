def hashtag(s):
    lista1=s
    a=len(s)//2
    lista2= "#"
    return lista2[0]+lista1[0:a]+lista2[0]+lista1[a:]+lista2[0]