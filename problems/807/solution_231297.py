def separa(f):
    a=f.split(".")
    b=a.split("!")
    c=b.split("?")
    d=c.split("...")
    return d

def conta_frases(f):
    return len(separa(f))