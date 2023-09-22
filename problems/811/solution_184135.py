def colchao(medidas,H,L):
    """Funcao que recebe em 'medidas' uma lista com as dimensoes do colchao em centimentos, ordenada do
menor para o maior, e dois inteiros H,L, correspondentes a altura e largura, respectivamente, das portas, em cm.
A funcao retorna True se o colchao passa pelas portas e False caso contrario"""
    if medidas[2]<=H and medidas[1]<=L:
        return True
    if medidas[1]<=H and medidas[0]<=L:
        return True
    if medidas[2]<=H and medidas[0]<=L:
        return True
    else:
        return False