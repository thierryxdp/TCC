def conta_frases(texto):
    """Conta o número de frases que aparecem no texto, que é o parâmetro
       str --> int"""
    a = str.count(texto,".")
    b = str.count(texto,"...") - 2
    c = str.count(texto,"?")
    d = str.count(texto,"!")
    return a + b + c + d