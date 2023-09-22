def conta_frases(frase):
    """Função que, dado um texto, retorna o número de frases
    que aparecem nesse texto. Cada frase no texto é terminada com
    um ponto final, um ponto de exclamação, um ponto de interrogação
    ou três pontos em sequência (reticências).
    str -> int"""
    frase1 = str.replace(frase, '!', '.')
    frase2 = str.replace(frase1, '?', '.')
    frase3 = str.replace(frase2, '...', '.')
    lista = str.split(frase3, '.')
    return len(lista) - 1