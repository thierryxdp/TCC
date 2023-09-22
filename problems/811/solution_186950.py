def colchao(medidas,H,L):
    """essa funçao recebe as dimensoes de um colchao e o tamanho de uma porta e retorna se e possievel o colchao atravessar ou nao a porta"""
    """entrada:list"""
    """saida:bool"""
    if medidas[0] >> H:
        return False
    else:
        return True