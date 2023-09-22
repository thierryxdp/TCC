def colchao(medidas,H,L):
    """essa funçao recebe as dimensoes de um colchao e o tamanho de uma porta e retorna se e possievel o colchao atravessar ou nao a porta"""
    """entrada:list"""
    """saida:bool"""
    if int(medidas[0])>>H or int(medidas[0])>>L:
        return 'false'
    if int(medidas[1])>>H or int(medidas[1])>>L:
        return 'false'
    if int(medidas[2])>>H or int(medidas[2])>>L:
        return 'false'
    else:
        return 'true'