def conta_frases (s):
    x = str.split(s)
    s1 = x[0:-1]
    if str.endswith(s1):
        return True
    else:
        return False