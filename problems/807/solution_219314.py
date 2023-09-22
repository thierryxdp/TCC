def conta_frases(frases):
    a=frases.count(".")
    b=frases.count("!")
    c=frases.count("?")
    d=frases.count("...")
    return (a+b+c-2*d)