def conta_frases(texto):
    """dado um texto entre aspas, a função retorna a quantidade de frases
    que o formam.
    strin-->int
    
    Parâmetros
    texto: texto utilizado como entrada para a contagem de frases"""
    return str.count(texto,".")+str.count(texto,"!")+str.count(texto,"?")-(2*(str.count(texto,"..."))