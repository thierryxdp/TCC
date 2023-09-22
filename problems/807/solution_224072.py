def conta_frases(frase):
    """Função que conta o número de frases que aparecem no texto"""
    """string -> int"""
    ponto = str.split(frase,".")
    interrogacao = str.split(frase,"?")
    exclamacao = str.split(frase,"!")
    reticencias = str.split(frase,"...")
    pontos = ponto+interrogacao+exclamacao+reticencias
    if reticencias >= 1:
        return pontos - reticencias*3
    return pontos