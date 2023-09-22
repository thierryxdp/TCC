def conta_frases(frases):
    a=frases.split(".")
    b=frases.split("!")
    c=frases.split("?")
    d=frases.split("...")
    return len(a+b+c+d)