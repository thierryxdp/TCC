def inverte(a):
    """apos obter a frase, vamos passo a passo separando a string a partir do termo
    indesejado e unindo-a de volta
    string->string"""
    f=a.split(".")
    f=''.join(f) 
    x=f.split(":")
    x=''.join(x)
    y=x.split(";")
    y=''.join(y)
    z=y.split("-")
    z=' '.join(z)
    q=z.split("?")
    q=''.join(q)
    d=q.split("!")
    d=''.join(d)
    i=d.split(",")
    i=' '.join(i)
    return i