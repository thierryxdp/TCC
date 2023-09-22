def inverte(frase):
    """essa funçao recebe uma string e retorna sem caracteres de pontuaçao e letras maiusculas a frase na ordem invertida"""
    a=frase.replace(","," ")
    b=a.replace("!"," ")
    c=b.replace("?"," ")
    d=c.replace("-"," ")
    e=d.replace(":"," ")
    f=e.replace(";"," ")
    g=f.replace("."," ")
    x=str.lower(g)
    s=x.split()
    j=str.join(" ",(s[::-1]))
    return j