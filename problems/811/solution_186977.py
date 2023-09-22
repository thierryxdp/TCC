def colchao(medidas,H,L):
    """essa funçao recebe as dimensoes de um colchao e o tamanho de uma porta e retorna se e possievel o colchao atravessar ou nao a porta"""
    """entrada:list,int"""
    """saida:bool"""
    if int(medidas[-2]) > int(H) and medidas[-1] > int(L):
        return False
    else: 
        return True