def conta_frases(frase):
    """funcao que da um texto ele retorna a quantidade de frases qeu ha nesse texto.
    str->int"""
    if "..." in frase:
        b=frase.count(".")
        c=frase.count("...")
        d=frase.count("!")
        e=frase.count("?")
        return b+c+d+e - 3*frase.count("...")
    else:
        b=frase.count(".")
        d=frase.count("!")
        e=frase.count("?")
        return b+d+e