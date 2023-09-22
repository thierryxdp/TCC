def conta_frases1(t):
    """Funcao retorna quantas frases existem em um texto dado no
    formato de string: t  """

    f1 = t.count("!")
    f2 = t.count("?")
    f3 = t.count("...")
    f4 = t.count(".") - (t.count("...")*3)

    caso1 = t[-1] != "!"
    caso2 = t[-1] != "?"
    caso3 = t[-1] != "."
    
    if caso1 and caso2 and caso3:
        return f1 + f2 + f3 + f4 + 1, "Esqueceu de por ponto no fim do texto."
    else:
        return f1 + f2 + f3 + f4