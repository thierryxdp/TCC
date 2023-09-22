def conta_frases(frase):
    a=frase
    a=a.split(".")
    a=map(str,a)
    a=a.join(" ")
    a=a.split("!")
    a=map(str,a)
    a=a.join(" ")
    a=a.split("?")
    a=map(str,a)
    a=a.join(" ")
    a=a.split("...")
    a=len(a)
    return a