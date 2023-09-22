def conta_frases(frase):
    """Função que conta o número de frases que aparecem no texto"""
    """string -> int"""
    frase = str.split(frase,".""!""?""...")
    return len(frase)