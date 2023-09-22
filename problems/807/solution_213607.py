def conta_frases(texto):
    """Dado um texto armazenado faça uma função que conte o número de frases que aparecem nesse texto.
    string -> string"""
    
    interrogacao = str.count(texto, "?") 
    ponto = str.count(texto, ".")
    exclamacao = str.count(texto, "!")
    tres = str.count(texto, "...")
    
    return interrogação + ponto + exclamação - três * 2