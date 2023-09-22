def colchao(medidas,H,L):
    ''' Recebe as medidas do colchão e da porta e retorna se é possivel passar com o colchão pela porta'''
    A,B = medidas[0],medidas[1]
    if B <= H and A <= 100:
        return True
    else:
       return False