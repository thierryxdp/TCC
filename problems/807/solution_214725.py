def conta_frases(texto):
    """Conta o número de frases que aparecem no texto, que é o parâmetro
       str --> int"""
    texto = str.replace("...", ".")
    a = str.count(texto,".")
    c = str.count(texto,"?")
    d = str.count(texto,"!")
    return a + c + d