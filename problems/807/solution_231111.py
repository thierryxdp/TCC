def conta_texto(x):
"""Função que recebe um texto e retorna o numero de frases
    do texto.
    str -> int"""
	if "!" in x:
        a=str.count(x,"!")
    if "!" not in x:
        a=0
    if "..." in x:
        b=str.count(x,"...")
    if "..." not in x:
        b=0
    if "?" in x:
        c=str.count(x,"?")
    if "?" not in x:
        c=0
    if "." in x:
        d=str.count(x,".")
    if "." not in x:
        d=0
    return a+b+c+(d-(3*b))