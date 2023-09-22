def inverte(frase):
    """ retorna uma nova frase que contém as mesmas palavras da frase de entrada na ordem inversa; str-->str"""
    frase = frase.lower()
    y=frase.replace(","," ")
    x=y.replace("."," ")
    z=x.replace(":"," ")
    a=z.replace("-"," ")
    b=a.replace(";"," ")
    c=b.replace("!"," ")
    d=c.replace("?"," ")
    e=d.split(" ")
    reversed_string ="".join(reversed(e))
    return reversed_string