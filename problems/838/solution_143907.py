import math

def num_bombons (din, pb):
    
    """Funçao que calcula o maior número de bombons
    que Pedrinho pode comprar com seu dinheiro. 
    Dados: din(dinheiro), pb(preço do bombom)"""
    
    return math.around(din/pb)