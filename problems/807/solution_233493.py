def conta_frases(frase):
    """Funçao que recebe uma string e conta o numero de frases no texto armazenado dentro dela.str -> int"""
    ponto = frase.count(".")
    interrogacao = frase.count("?")
    exclamacao = frase.count("!")
    reticencias = frase.count("...")
    frase_c_reticencias = (reticencias*3)
    if "..." in frase:
        return (ponto+interrogacao+exclamacao+reticencias-frase_c_reticencias)
    else:
        return (ponto+interrogacao+exclamacao)