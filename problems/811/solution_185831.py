# Dada as medidas de um colchão, A, B e C, em uma lista,
# retorna se é possível passa-lo por uma porta de altura H e largura L
# lista, int, int -> boolean
def colchao(medidas, H, L):
    B, C = medidas[1], medidas[2]
    if((B > H and B > L) and (C > H and C > L)):
        return False
    return True