def separa(f):
    a=f.split(". ")
    b=f.split("...")
    c=f.split("?")
    d=f.split("!")
    return a+b+c+d
def conta_frases(f):
    return len(separa(f))