def inverte(frase):
    """ retorna uma nova frase que contém as mesmas palavras da entrada na ordem invvers; str-->str"""
    y=frase.replace(","," ")
    x=y.replace("."," ")
    z=x.replace(":"," ")
    a=z.replace("-"," ")
    b=a.replace(";"," ")
    c=b.replace("!"," ")
    d=c.replace("?"," ")
    e=d.split(" ")
    reversed_string =" ".join(reversed(e))
    return reversed_string