def conta_frases(texto):
    """Função que calcula e retorna a quantidade de frases dado
    um texto, cada frase termina com um ponto finalizador
    str-> int"""
    a = texto.count(str("."))
    b = texto.count(str("!"))
    c = texto.count(str("?"))
    d = texto.count(str("..."))*3
    return a + b + c - d