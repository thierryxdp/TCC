def conta_frases(f):
    a=f.split(". ")
    b=a.split("!")
    c=b.split("...")
    d=c.split("?")
    return len(d)