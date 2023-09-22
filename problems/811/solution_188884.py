def colchao(medidas,H,L):
    """Função que recebe as medidas de um colchão e de uma porta e verifica se o colchão consegue passar pela porta
    entrada:list,int,int
    saída:bool"""
    if medidas[0]<= H and medidas[1]<= L:
        return True
    else:
        return False