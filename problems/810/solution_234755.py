def inverte(frase):
    sep = str.split(frase," ")
    return str.join((sep[-1],sep[0],-1),sep)

"""
(frase[-1],frase[0],-1)
"""