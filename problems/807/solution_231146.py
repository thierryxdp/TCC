def conta_frases(frase):
    """Recebe uma string e conta o número de frases que aparecem nela. str -> int."""
    r= 0
    if str.partition(frase,'...'):
        r=r+1
    if str.partition(frase,'.'):
        r= r+1
    if str.partition(frase,'!'):
        r=r+1
    if str.partition(frase,'?'):
        r=r+1
    return r