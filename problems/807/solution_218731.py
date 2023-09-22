def conta_frases(texto):
    """inserindo um texto mostra o numero de frases que ele tem"""
    pontuacoes = ("...","!","?",".")
    for pontuacao in pontuacoes:
        texto = texto.replace(pontuacao,(pontuacao) +"  ")
    return (len(texto.split("  "))-1)