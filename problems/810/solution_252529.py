def inverte(frase):
    '''função que, dada uma frase de entrada, retorna uma outra frase
    que contenha as mesmas palavras da frase de entrada,
    mas na ordem inversa, sem letras maiusculas e sem a pontuação;
    str-->list'''
    y=frase.replace("-","")

    x=y.replace("!","")

    z=x.replace(";","")

    p=z.replace(", ","")

    q=p.replace(".","")

    r=q.replace(":","")

    s=r.replace("?","")

    t=s.replace("!","")

    a=str.lower(t)

    b=str.split(a)

    c=b[::-1]

    d=str.join("  ",c)

    return d