def conta_frases(frase):
    l1 = frase.split(".")
    l2 = l1.split("!")
    l3 = l2.split("?")
    l4 = l3.split("...")
    return len(l4)