def colchao(medidas,H, L):
    """
    Função que dada as medidas de um colchão, a altura e largura de uma porta, retorna true se o colchão passar por essa porta e false, se não passar
    list, int, int-> bool
    
    Parameters:
    medidas: Parâmetro do tipo lista que contém 3 números inteiros que representam o tamanho do colchão
    H: Parâmetro do tipo int que representa a altura da porta
    L: Parâmetro do tipo int qu representa a largura da porta
    """
    A,B,C = medidas 

    if A and B > H and L:
        return False
    else:
        return True