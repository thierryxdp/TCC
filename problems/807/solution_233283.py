def conta_frases(f):
    a=f.split(".")
    a=f.split("!")
    a=f.split("...")
    a=f.split("?")
    return len(a)