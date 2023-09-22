def conta_frases(texto):
    """Funçao que, dado um texto armazenado em uma string, calcula o número de frases que aparecem nesse texto
       Cada frase pode ser terminada com ponto final, ponto de exclamaçao, ponto de interrogaçao ou reticencias
       str->int"""
    return str.count(texto,". ")+ str.count(texto,"! ")+ str.count(texto,"? ")+ 1