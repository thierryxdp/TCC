def conta_frase(x):
    """
Função que dado uma strng conta as frases a partir dos pontos '.', '!', '?', '...'
"""
    r = int()
    if "." in str(x):
        r = r + (len(str.split(x,"."))-1)
    if "?" in str(x):
        r = r + len((str.split(x,"?"))-1)
    if "..." in str(x):
        r = r + len((str.split(x,"..."))-1)
    if "!" in str(x):
        r = r + len(str.split((x,"!"))-1)
    return int(r)