def conta_frases (s):
    nf = 0
    ne = 0
    ni = 0
    nr = 0
    if "." in s:
        nf = str.count (s, ".")
    if "!" in s:
        ne = str.count (s, "!")
    if "?" in s:
        ni = str.count (s, "?")
    if "..." in s:
        nr = str.count (s, "...")
    return nf + ne + ni + nr