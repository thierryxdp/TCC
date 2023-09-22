def passa(colchao, portah, portal):
    """recebe uma lista contendo as medidas do colchao, em centimetros,
    ordenadas da menor para a maior, e dois inteiros que representam,
    respectivamente, a altura e a largura das portas de uma casa; retorna
    True ou False se o colchao consegue passar, ou nao, pela porta
    list, int, int -> bool"""
    
    if (colchao[1] <= portah or colchao[1] <= portal or colchao[2] <= portah or colchao[2] <= portal):
        return True
    
    else: 
        return False