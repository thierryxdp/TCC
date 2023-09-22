def colchao(medidas,H,L):
    """ essa função tem como finalidade retornar true se o colchao ira passar pela porta e false caso não consiga passar
    entrada -> list, int, int
    saida -> booleano """
    a,b,c = medidas
    if b > H and c > H:
        return False
    elif a > L:
        return False
    elif b <= H or c <= H:
        return True
    else:
        return True