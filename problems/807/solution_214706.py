def conta_frases(frase):
    """funcao que da um texto ele retorna a quantidade de frases qeu ha nesse texto.
    str->int"""
    a=str.split(frase)
    b=list.count(a,".")
    c=list.count(a,"...")
    d=list.count(a,"!")
    e=list.count(a,"?")
    return b+c+d+e