def colchao(medidas,H,L):
    """Função que recebe as medidas de um colchão e de uma porta e verifica se o colchão consegue passar pela porta
    entrada:list,int,int
    saída:bool"""
    if medidas[0]<= L and medidas[1]<= H or medidas[1]<= H and medidas[2]<= L:
        return True
    else:
        return False