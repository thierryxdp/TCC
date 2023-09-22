def inverte(frase):
    """Calcula e inverte a frase"""
    y=frase.replace("-","")
    x=y.replace("!","")
    z=x.replace(";","")
    p=z.replace(",","")
    q=p.replace(".","")
    r=q.replace(":","")
    s=r.replace("?","")
    t=s.replace("!","")
    a=str.lower(t)
    b=split(a,"")
    c=list.reverse(b)
    d=str.join("",c)
    return d