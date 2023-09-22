def colisao(tup1,tup2):
    """funçao c que, dados dois retangulos, determine se eles se interceptam(True) ou nao(False) tuple, tuple --> bool"""
    if tup1[2] < tup2[0] or tup1[0] > tup2[2] or tup1[3] < tup2[1] or tup1[1] > tup2[3]:
        return False
    else:
        return True