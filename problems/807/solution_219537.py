def conta_frases(frase):
    """Função que, conte o número de frases que aarecem  no texto.
    str -> int"""
     
    f1 = frase.cont(".")
    f2 = frase.cont("!")
    f3 = frase.cont("...")
    f4 = frase.cont("?")
      
    return f1+f2+f3+f4