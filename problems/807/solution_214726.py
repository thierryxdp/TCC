def conta_frases(texto):
    """Conta o número de frases que aparecem no texto, que é o parâmetro
       str --> int"""
    texto = texto.replace("...", ".")
    a = str.count(texto,".")
    b = str.count(texto,"?")
    c = str.count(texto,"!")
    return a + b + c