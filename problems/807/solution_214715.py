def conta_frases(texto):
    """Conta o número de frases que aparecem no texto, que é o parâmetro
       str --> int"""
    a = texto.count(texto,".")
    b = texto.count(texto,"...")
    c = texto.count(texto,"?")
    d = texto.count(texto,"!")
    return a + b + c + d