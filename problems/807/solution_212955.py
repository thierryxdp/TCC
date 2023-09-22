def conta_frases(texto):
    """Retorna a quantidade de frases em um texto. str-->int"""
    n=str.count(texto,"!")+str.count(texto,"?") str.count(texto,".") 
    r=str.count(texto,"...")
    return n-r