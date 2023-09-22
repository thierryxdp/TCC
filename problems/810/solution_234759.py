def inverte(frase):
    sep = str.split(frase," ")
    inv = (sep[-1],sep[0],-1)
    return str.join(inv)

"""
(frase[-1],frase[0],-1)
"""