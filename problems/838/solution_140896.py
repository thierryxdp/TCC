def num_bombons(p,d)
    """Função que calcula e retorna o número de bombons que podem ser
    comprados dados o preço unitário p e o dinheiro d disponível para a 
    realização da compra"""
    return round((d/p)-0.5)