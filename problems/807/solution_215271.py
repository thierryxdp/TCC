def conta_frases(frase):
    a=frase
    a=a.split(".")
    a=a.join(" ")
    a=a.split("!")
    a=a.join(" ")
    a=a.split("?")
    a=a.join(" ")
    a=a.split("...")
    a=len(a)
    return a