def conta_frases(texto):
    """Função que calcula e retorna a quantidade de frases dado
    um texto, cada frase termina com um ponto finalizador
    str-> int"""
    a = texto.count(".")
    b = texto.count("!")
    c = texto.count("?")
    d = texto.count("...")
    return a + b + c + d