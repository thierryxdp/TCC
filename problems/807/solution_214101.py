def quant_frases(t):
"""Funcao retorn quantas frases existem em um texto dado no
    formato de string: t  """

    f1 = t.split("...")

    s = str.join(" ", f1)

    f2 = s.split(".")

    f3 = t.split("?")

    f4 = t.split("!")

    if type(f1) == str:
        nf1 = 0
    else:
        nf1 = len(f1)-1
        
    if type(f2) == str:
        nf2 = 0
    else:
        nf2 = len(f2)-1

    if type(f3) == str:
        nf3 = 0
    else:
        nf3 = len(f3)-1

    if type(f4) == str:
        nf4 = 0
    else:
        nf4 = len(f4)-1

    return nf1 + nf2 + nf3 + nf4