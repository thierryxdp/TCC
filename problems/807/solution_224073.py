def conta_frases(frase):
    """Função que conta o número de frases que aparecem no texto"""
    """string -> int"""
    ponto = frase.count(frase,".")
    interrogacao = frase.count(frase,"?")
    exclamacao = frase.count(frase,"!")
    reticencias = frase.count(frase,"...")
    pontos = ponto+interrogacao+exclamacao+reticencias
    if reticencias >= 1:
        return pontos - reticencias*3
    return pontos