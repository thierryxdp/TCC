def separa(f):
    a=f.split(". ")
    b=f.split("!")
    c=f.split("...")
    d=f.split("?")
    s=0
    s+=a+=b+=c+=d
    return s

def conta_frases(f):
    return len(separa(f))