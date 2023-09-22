def colchao(medidas, H, L):
    """recebe uma lista contendo as medidas do colchao, em centimetros,
    ordenadas da menor para a maior, e dois inteiros que representam,
    respectivamente, a altura e a largura das portas de uma casa; retorna
    True ou False se o colchao consegue passar, ou nao, pela porta
    list, int, int -> bool"""
    
    if (medidas[1] <= H or medidas[1] <= L or medidas[2] <= H or medidas[2] <= L):
        return True
    
    else: 
        return False