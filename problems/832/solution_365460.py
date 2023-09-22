# Questão 1
def eh_quadrada(matriz):
    t2 = len(matriz)
    if t2 == 0:
        return True
    
    t1 = len(matriz[0])

    if t1 == t2:
        return True
    else:
        return False