def inverte(frase):
    '''função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa
    str-->str'''
    x=frase.replace("-","")
    y=x.replace(",","")
    z=y.replace("!","")
    j=z.replace(":","")
    k=j.replace(";","")
    l=k.replace(".","")
    f=l.replace("?","")
    a=str.lower(f)
    b=str.split(a)
    c=b[::-1]
    d=str,join(" ",c)
    return d