def conta_frases(texto):
    """Dado um texto, conta o número de frases que aparecem nesse texto, Cada frase no texto é terminada com um ponto, seja final, exclamaçao, interrogaçao ou reticecias
    entrada: str
    saida: str"""
    x="!", "?", ".", "..."
    return texto.split(x)