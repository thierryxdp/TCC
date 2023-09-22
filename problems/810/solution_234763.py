def inverte(frase):
    sep = str.split(" ")
    inv = (frase[-1],frase[0],-1)
    return str.join(inv,sep)

"""
(frase[-1],frase[0],-1)
"""