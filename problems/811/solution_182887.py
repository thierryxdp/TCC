def colchao (medidas, H, L):
    """ funcao ira receber medidas de um colchao e calcular seu tamanho exate. Caso esse passe pela porta ira retornar True, caso contrario retorna false."""
    if L >= medidas[0] and H >= medidas[1]:
        return True
    else:
        return False