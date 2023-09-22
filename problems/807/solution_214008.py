def conta_frases (s):
    x = str.split(s)
    s1 = x[0:]
    if str.endswith("!"):
        return True
    else:
        return False