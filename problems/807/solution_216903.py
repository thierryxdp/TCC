def conta_frases (a = str) -> int:
    """Função que dado um texto armazenado em uma string, faça a função que conte o número de frases que aparecem nesse texto. Cada frase no texto é terminada com um ponto final, um ponto de exclamação, um ponto de interrogação ou três reticências."""
    x = str.split(str.replace(str.replace(str.replace(a, "!", "."), "?", "."), "...", "."), ".")
    
    return len(x)-1