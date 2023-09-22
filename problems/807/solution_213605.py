def conta_frases(texto):
    """Dado um texto armazenado faça uma função que conte o número de frases que aparecem nesse texto.
    string -> string"""
    
    interrogação = str.count(texto, "?") 
    ponto = str.count(texto, ".")
    exclamação = str.count(texto, "!")
    três = str.count(texto, "...")
    
    return interrogação + ponto + exclamação - três * 2