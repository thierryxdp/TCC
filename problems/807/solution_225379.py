def conta_frases(texto):
    """Função que conta a quantidade de frases em um texto."""
    """string->int"""
    ponto=['.','!','...','?']
    if "..." and "." in texto:
        reticencias=(texto.count("...")*3)
        return sum([texto.count(i) for i in ponto])-reticencias
    else:
        return sum([texto.count(i) for i in ponto])