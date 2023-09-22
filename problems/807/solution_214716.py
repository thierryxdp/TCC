def conta_frases(texto):
    """Conta o número de frases que aparecem no texto, que é o parâmetro
       str --> int"""
    a = int texto.count(texto,".")
    b = int texto.count(texto,"...")
    c = int texto.count(texto,"?")
    d = int texto.count(texto,"!")
    return a + b + c + d