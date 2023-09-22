def inverte(a):
    """apos obter a frase, vamos passo a passo separando a string a partir do termo
    indesejado e unindo-a de volta, depois que tiramos a pontuacao utilizamos
    lower para colocar em minusculo e transformamos em lista mais uma vez para
    inverter a ordem apresentada, finalmente retornando uma nova string
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
    i=''.join(i)
    i=i.lower()
    i=i.split(" ")
    i=i[::-1]
    i=" ".join(i)
    return i