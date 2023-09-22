def separa(f):
    return list(f.split(".")+f.split("!")+f.split("?")+f.split("..."))
def conta_frases(f):
    return len(separa(f))