def inverte(frase):
    '''coloca a frase de tras pra frente'''
    l1 = frase.split("!")
    l2 = " ".join(l1)
    l3 = l2.split("?")
    l4 = " ".join(l3)
    l5 = l4.split("...")
    l6 = " ".join(l5)
    l7 = l6.split(".")
    l8 = " ".join(l7)
    l9 = l8.split(",")
    l10 = " ".join(l9)
    l11 = l10.split("-")
    l12 = " ".join(l11)
    return (l12[::-1])

    l1 = frase.plit
    l1.reverse()
    frase = frase.join(" ", l1)
    return frase