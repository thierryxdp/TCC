conta_frases(texto):
    """Conta o número de frases que aparecem no texto, que é o parâmetro
       str --> int"""
    a = texto.count(string,".")
    b = texto.count(string,"...")
    c = texto.count(string,"?")
    d = texto.count(string,"!")
    texto = a + b + c + d