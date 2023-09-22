def conta_frases(txt):
    a = txt.split("...")
    a = a + txt.split(".")
    a = a + txt.split("!")
    a = a + txt.split("?")
    return len(a)