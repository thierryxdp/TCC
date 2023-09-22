def inverte(frase):
    sep = frase.split(" ")
    inv = (frase[-1],frase[0],-1)
    return str.join(sep,inv)

"""
(frase[-1],frase[0],-1)
"""