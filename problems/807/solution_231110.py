def conta_frases(x):
    """Função que recebe um texto como entrada e retorna 
    a quantidade de frases no texto.
    str -> int"""
    if "!" in x:
        a=str.count(x,"!")
    if "..." in x:
        b=str.count(x,"...")
    if "?" in x:
        c=str.count(x,"?")
    if "." in x:
        d=str.count(x,".")
    return a+b+c+(d-(3*b))