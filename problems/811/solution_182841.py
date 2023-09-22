def colchao(medidas, H, L):
    '''Dadi as dimensões do colchão AxBxC em cm(representada por umalista)e a altura(H) e a 
    largura(L) da porta, retorna se é possivel passar o colchão ou não.
    lista, float, float, float -> bool'''
    A, B, C = medidas
    a1 = min(A, B, C)
    a3 = max(A,B,C)
    a2 = (A+B+C) - a1-  a3
    if a1 <= min(H, L) and  a2 <= max(H,L):
        return True
    else:
        return False