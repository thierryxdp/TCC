def conta_frases(frase):
    l1 = frase.split("!")
    l2 = ".".join(l1)
    l3 = l2.split("?")
    l4 = ".".join(l3)
    l5 = l4.split("...")
    l6 = ".".join(l5)
    l7 = l6.split(".")
    return l7