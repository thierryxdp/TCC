def conta_frases(txt):
    a = txt.strip("...")
    a = a + txt.strip(".")
    a = a + txt.strip("!")
    a = a + txt.strip("?")
    return len(a)