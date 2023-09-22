def conta_frases1(t):
    """Funcao retorn quantas frases existem em um texto dado no
    formato de string: t  """

    f1 = t.count("!")
    f2 = t.count("?")
    f3 = t.count("...")
    f4 = t.count(".") - (t.count("...")*3)
    
    return f1 + f2 + f3 + f4