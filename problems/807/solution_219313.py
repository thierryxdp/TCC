def conta_frases(frases):
    a=frases.count(".",1)
    b=frases.count("!")
    c=frases.count("?")
    d=frases.count("...")
    return (a+b+c+d)