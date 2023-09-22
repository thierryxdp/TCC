def conta_frases(txt):
    a = txt.strip("...")
    a = a.strip(".")
    a = a.strip("!")
    a = a.strip("?")
    return len(a)