# def colchao(medida, H, L):
    """Dado tres dimensoes de um colchao em centimetros, verifica se esse colchao tem as medidas"""
    [A, B, C] = medidas
    if A and B > H and L:
        return False
    else:
        return True
Coloque um comentário dizendo o que a função faz