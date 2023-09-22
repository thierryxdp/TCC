def separa(f):
    return f.split((".")+("...")+("?")+("!"))
def conta_frases(f):
    return f.count(separa(f))