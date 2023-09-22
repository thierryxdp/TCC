def conta_frases (s):
    if "." in s:
        nf = str.count (s, ".")
    if "!" in s:
        ne = str.count (s, "!")
    if "?" in s:
        ni = str.count (s, "?")
    if "..." in s:
        nr = str.count (s, "...")
    return nf + ne + ni + nr