def frasecont(palavras):
    inter=str.count(palavras, "?")
    excl=str.count(palavras, "!")
    ponto =str.count(palavras, ".")
    ret=0
    if "..." in palavras :
        ret=str.count(palavras, "...")
        ponto = ponto-3
    return inter+ret+excl+ponto