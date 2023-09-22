def conta_frases(texto):
    """conta o número de frases que aparecem no texto;
    string -> tupla"""
    
    texto = texto.split(".,!,?,...")
    x = len(texto)