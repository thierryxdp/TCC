def conta_frases(frases):
    v=str.split(frases,"!")
    exclamacao=len(v)
    x=str.split(frases,".")
    ponto=len(x)
    y=str.split(frases,"...")
    trespontos=ponto/3
    z=str.split(frases,"?")
    interrogacao=len(z)
    return exclamacao-1+ponto-1+trespontos-1+interrogacao-1