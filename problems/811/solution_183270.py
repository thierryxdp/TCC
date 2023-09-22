def colchao(medidas:list,H:int,L:int)->bool:
    """Dadas as medidas de um colchão e a altura H e a largura L de uma porta, calcula e retorna se é possível esse colchão passar pela porta (retornando True) ou não (retornando False) ."""
    if medidas[0] > H and medidas[1] > H:
        return False
    elif medidas[0] > H and medidas[2] > H:
        return False
    elif medidas[2] > H and medidas[1] > H:
        return False
    else: return True