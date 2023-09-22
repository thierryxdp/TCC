def conta_frases(frase):
    """Função que conta o número de frases que aparecem no texto"""
    """string -> int"""
    ponto = frase.count(".")
    interrogacao = frase.count("?")
    exclamacao = frase.count("!")
    reticencias = frase.count("...")
    pontos = ponto+interrogacao+exclamacao+reticencias
    if reticencias >= 1:
        return pontos - reticencias*3
    return pontos