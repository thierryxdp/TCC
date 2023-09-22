def inverte (frase):
    """Calcula e retorna a variavel de entrada frase 
    na ordem inversa, sem letra maiuscula e sem
    pontuacao; str --> str"""
    y=frase.replace("-"," ")
    x=y.replace("!"," ")
    z=x.replace(";"," ")
    p=z.replace(","," ")
    q=p.replace("."," ")
    r=q.replace(":"," ")
    s=r.replace("?"," ")
    t=s.replace("!"," ")
    a=str.lower(t)
    b=str.split(a)
    c=b[::-1]
    d=str.join(" ",c)
    return d