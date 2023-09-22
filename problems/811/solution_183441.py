def colchao(medidas, H, L):
    """Função que retorna se um colchão passa pela porta, dadas as medidas do colchão e
    das medidas da altura H e da largura H da porta
    entrada: lista(int, int, int)
    retorno: bool"""
    if medidas[0]< L and medidas[2]< H:
        return True
    elif medidas[0]< L and medidas[1]< H:
        return True
    else:
        return False